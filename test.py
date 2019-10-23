import unittest

from xsd_download import (remove_comments_from_xml,
                          url_to_path,
                          localize_links,
                          # save_file,
                          # download_url,
                          # recursive_get_schema_locations
                          )


class TestXSDDownload(unittest.TestCase):
    """Tests for xsd_download."""

    def test_remove_comments_from_xml(self):
        self.assertEqual('<xml>abc</xml>',
                         remove_comments_from_xml
                         (b'<xml>abc<!-- comment --></xml>'))

    def test_url_to_path(self):
        self.assertEqual('example.com/test/a/b/c/',
                         url_to_path('http://example.com/test/a/b/c/'))

    def test_localize_links(self):
        self.assertEqual(
            localize_links('schemaLocation="http://example.com/a/blah.xsd"',
                           'example.com/a/blah.xsd'),
            'schemaLocation="./blah.xsd"')


if __name__ == '__main__':
    unittest.main()
