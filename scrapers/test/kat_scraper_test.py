import unittest2 as unittest
from kat_scraper import KatScraper

class TestKatScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = KatScraper()
            
    def test_get_torrent(self):
        self.assertTrue(len(self.scraper.get_torrents('ubuntu')) > 0)

    def test_get_no_torrent(self):
        self.assertTrue(len(self.scraper.get_torrents('thisstringmustnotexistsssssssssaaaaaassss')) == 0)


if __name__ == '__main__':
    unittest.main()
