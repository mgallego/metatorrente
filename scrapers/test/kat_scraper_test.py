import unittest2 as unittest
from kat_scraper import KatScraper

class TestKatScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = KatScraper()
            
    def test_get_torrent(self):
        self.assertTrue(len(self.scraper.get_torrents('ubuntu')) > 0)

    def test_get_no_torrent(self):
        self.assertTrue(len(self.scraper.get_torrents('thisstringmustnotexistsssssssssaaaaaassss')) == 0)

    def test_torrent_document_keys(self):
        torrent = self.scraper.get_torrents('ubuntu')[0]
        self.assertTrue('name' in torrent)
        self.assertTrue('magnet' in torrent)
        self.assertTrue('seed' in torrent)
        self.assertTrue('leech' in torrent)

if __name__ == '__main__':
    unittest.main()
