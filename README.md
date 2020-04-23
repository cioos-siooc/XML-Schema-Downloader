# Recursive .xsd Schema downloader

Use this Python 3 script to recursively download an XSD schema and all linked schemas. This lets you quickly validate an xml record using a tool such as `xmllint`.

It supports relative XSD schemaLocations, eg `<import schemaLocation="../../../../abc`.

## Installation

If needed, install `virtualenv`

`pip install virtualenv --user`

Create and activate a new Python 3 environment:
`virtualenv -p python3 venv`
`source venv/bin/activate`

Install requirements:
`pip install -r requirements.txt`

## Running

Run the script with your favorite .xsd URL:

`python xsd_download.py https://standards.iso.org/iso/19115/-3/mdb/1.0/mdb.xsd`

Your schema ends up in a folder called 'xsd'

## Schema validation with xmllint

Then if you have `xmllint` installed, you can validate an XML file called `myrecord.xml` by running:

`xmlllint --noout --schema ./xsd/standards.iso.org/iso/19115/-3/mdb/1.0/mdb.xsd myrecord.xml`

## Run tests

`python tests.py`
