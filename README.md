# XML Schema Downloader

[![GitHub Super-Linter](https://github.com/n-a-t-e/xsd_download/workflows/Lint%20Code%20Base/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Python package](https://github.com/cioos-siooc/XML-Schema-Downloader/actions/workflows/python.yaml/badge.svg)](https://github.com/cioos-siooc/XML-Schema-Downloader/actions/workflows/python.yaml)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

Use this Python script to recursively download an XML schema (XSD) and all linked schemas. This lets you quickly validate an xml record using a tool such as `xmllint`.

It supports relative XSD schemaLocations, eg `<import schemaLocation="../../../../abcd`.

## Installation

If needed, install `virtualenv`. Install repository in a new Python 3 environment:

```sh
pip install venv --user
python -m venv venv
source venv/bin/activate
pip install .
```

## Running

Run the script with your favorite .xsd URL:

`python -m xsd_download https://schemas.isotc211.org/19115/-3/mdb/2.0/mdb.xsd`

Your schema ends up in a folder called 'xsd'

## Schema validation with xmllint

Then if you have `xmllint` installed, you can validate an XML file called `myrecord.xml` by running:

`xmllint --noout --schema ./xsd/schemas.isotc211.org/19115/-3/mdb/2.0/mdb.xsd myrecord.xml`

## Run tests

`python tests/tests.py`

## Docker

You can create a Docker image containing the script. This way you don't need to setup any python and venv.

### Build image

```shell
docker build -t cioos-siooc/xml-schema-downloader:1.0 .

```

### Run image

Run the image with your favorite .xsd URL:

```shell
docker run --rm -v `pwd`:`pwd` -w `pwd` cioos-siooc/xml-schema-downloader:1.0 https://schemas.isotc211.org/19115/-3/mdb/2.0/mdb.xsd

```
