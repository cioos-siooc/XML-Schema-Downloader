# XML Schema Downloader

[![GitHub Super-Linter](https://github.com/n-a-t-e/xsd_download/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)

Use this Python script to recursively download an XML schema (XSD) and all linked schemas. This lets you quickly validate an xml record using a tool such as `xmllint`.

It supports relative XSD schemaLocations, eg `<import schemaLocation="../../../../abc`.

## Installation

If needed, install `virtualenv`. Install repo in a new Python 3 environment:

```sh
pip install venv --user
python -m venv venv
source venv/bin/activate
pip install .
```

## Running

Run the script with your favorite .xsd URL:

`python -m xsd_download https://standards.iso.org/iso/19115/-3/mdb/1.0/mdb.xsd`

Your schema ends up in a folder called 'xsd'

## Schema validation with xmllint

Then if you have `xmllint` installed, you can validate an XML file called `myrecord.xml` by running:

`xmllint --noout --schema ./xsd/standards.iso.org/iso/19115/-3/mdb/1.0/mdb.xsd myrecord.xml`

## Run tests

`python tests/tests.py`
