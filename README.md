# Recursive XSD downloader

Use this Python 3 script to recursively download an XSD schema and all linked schemas.

It supports relative XSD schemaLocations, eg `<import schemaLocation="../../../../abc`.

# Instalation

Active your python3 environment, eg:
`source activate python3`

Install requirements:
`pip install -r requirements.txt`

# Running

Run the script with your favorite XSD:
`python xsd_download.py https://standards.iso.org/iso/19115/-3/mdb/1.0/mdb.xsd`

Your schema ends up in a folder called 'xsd'
