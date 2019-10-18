import os
import re
import urllib.request
from urllib.parse import urljoin, urlparse
import click

XSD_DIR = 'xsd'


def url_to_path(url):
    'turns a URL to an XSD into a filesystem path'
    parsed = urlparse(url)
    # file structure like ./www.example.come/a/b/c.xsd
    path = parsed.netloc + parsed.path
    return path


def localize_links(url, text, filename_complete):
    """ Similar to wget's --convert-links, this converts the schemaLocation
        links to be useable on local filesystem
    """
    schema_locations = re.findall('schemaLocation="(http.*)"', text)

    for schema_location in schema_locations:
        path_url = url_to_path(schema_location)
        rel_path = os.path.relpath(
            os.path.dirname(path_url), os.path.dirname(filename_complete))
        base_name = os.path.basename(path_url)
        text = text.replace(schema_location, rel_path + '/' + base_name)
    return text


def save_file(url, text):
    'save the XSD `text` data to file path decided by `url`'
    filename_complete = url_to_path(url)
    dir_name = os.path.dirname(XSD_DIR + '/' + filename_complete)

    # create directory structure
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    f = open(XSD_DIR + '/' + filename_complete, "w")
    text_localized = localize_links(url, text, filename_complete)
    f.write(text_localized)
    f.close()


def download_url(url):
    'Fetches URL, returns text of the document'
    response = urllib.request.urlopen(url)
    return response.read().decode('utf-8')


# list of the URLs that have been downloaded already
downloaded_urls = []


def recursive_get_schema_locations(url):
    """ Recursive function that is the heart of the script,
        stops when... TODO
    """
    # dont download same link twice
    if url not in downloaded_urls:
        downloaded_urls.append(url)
        try:
            xsd_data = download_url(url)
        except urllib.error.URLError as e:
            print('ERROR loading {} REASON: {} '.format(url, e.reason))
            return
        # all the XSDs linked from this file via schemaLocation
        schema_locations = re.findall('schemaLocation="(.*)"', xsd_data)

        # write this file in the directory structure
        save_file(url, xsd_data)

        # iterate through all schemaLocation URLs
        for schema_location in schema_locations:
            # urljoin translates relative URLs in schemaLocation to absolute
            # eg:
            # >>> urljoin('http://example.com/1/2/3','../../index.html')
            # turns into: http://example.com/index.html

            line = urljoin(url, schema_location)
            print(line)
            recursive_get_schema_locations(line)


@click.command()
@click.argument('xsd_url')
def main(xsd_url):
    """Recursive xsd downloader that suports relative imports"""
    print("Downloading schema files:")
    recursive_get_schema_locations(xsd_url)


if __name__ == '__main__':
    main()
