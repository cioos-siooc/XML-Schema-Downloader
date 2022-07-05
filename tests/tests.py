import unittest

from xsd_download.xsd_download import localize_links, url_to_path


class TestXSDDownload(unittest.TestCase):
    """Tests for xsd_download."""

    def test_url_to_path(self):
        self.assertEqual(
            "example.com/test/a/b/c/", url_to_path("http://example.com/test/a/b/c/")
        )

    def test_localize_links(self):
        self.assertEqual(
            localize_links(
                'schemaLocation="http://example.com/a/blah.xsd"',
                "example.com/a/blah.xsd",
            ),
            'schemaLocation="./blah.xsd"',
        )


if __name__ == "__main__":
    unittest.main()
