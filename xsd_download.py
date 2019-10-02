import os
import re
import urllib.request
from urllib.parse import urljoin
from urllib.parse import urlparse
from os.path import relpath
import click

# eg: python xsd_download.py https://standards.iso.org/iso/19115/-3/mdb/1.0/mdb.xsd


def url_to_path(url):
    parsed = urlparse(url)
    path = './' + parsed.netloc + parsed.path
    return path


def save_file(url, text):
    filename_complete = url_to_path(url)
    dirname = os.path.dirname(filename_complete)

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    f = open(filename_complete, "w")
    text_localized = localize_links(url, text, filename_complete)
    f.write(text_localized)
    f.close()


def download_url(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    return text


downloaded = []


def recursive_get_schema_locations(url):
    # dont download same link twice
    if url not in downloaded:
        downloaded.append(url)
        try:
            data = download_url(url)
        except urllib.error.URLError as e:
            print('ERROR loading {} REASON: {} '.format(url, e.reason))
            return
        schema_locations = re.findall('schemaLocation="(.*)"', data)
        save_file(url, data)
        for schema_location in schema_locations:
            line = urljoin(url, schema_location)
            print(line)
            recursive_get_schema_locations(line)


def localize_links(url, text, filename_complete):
    schema_locations = re.findall('schemaLocation="(http.*)"', text)

    for schema_location in schema_locations:
        path_url = url_to_path(schema_location)
        rel_path = relpath(
            os.path.dirname(path_url), os.path.dirname(filename_complete))
        base_name = os.path.basename(path_url)
        text = text.replace(schema_location, rel_path + '/' + base_name)
    return text


@click.command()
@click.argument('xsd_url')
def main(xsd_url):
    print("Downloading schema files:")
    recursive_get_schema_locations(xsd_url)


if __name__ == '__main__':
    main()
