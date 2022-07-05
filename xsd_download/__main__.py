import click

from xsd_download.xsd_download import download_schema


@click.command()
@click.argument("xsd_url")
def main(xsd_url: str):
    """Recursive xsd downloader that suports relative imports"""
    print("Downloading schema files:")
    download_schema(xsd_url)


if __name__ == "__main__":
    main()
