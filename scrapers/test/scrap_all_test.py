import unittest2 as unittest
from scrap_all import ScrapAll

class TestKatScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = ScrapAll()
            
    def test_get_torrent(self):
        self.assertTrue(len(self.scraper.get_torrents('ubuntu')) > 0)

    def test_get_no_torrent(self):
        self.assertTrue(len(self.scraper.get_torrents('thisstringmustnotexistsssssssssaaaaaassss')) == 0)

    def test_torrent_document_keys(self):
        torrent = self.scraper.get_torrents('ubuntu')[0]
        self.assertTrue('name' in torrent)
        self.assertTrue('link' in torrent)
        self.assertTrue('magnet' in torrent)
        self.assertTrue('seed' in torrent)
        self.assertTrue('leech' in torrent)
        self.assertTrue('size' in torrent)
        self.assertTrue('site' in torrent)

    def test_torrent_name(self):
        torrent = self.scraper.get_torrents('ubuntu')[0]
        self.assertTrue('buntu' in torrent['name'])

    def test_sort(self):
        torrents = self.scraper.get_torrents('ubuntu')
        self.assertTrue(torrents[0]['seed'] > torrents[1]['seed'])
        self.assertTrue(torrents[1]['seed'] > torrents[2]['seed'])
        self.assertTrue(torrents[2]['seed'] > torrents[3]['seed'])
        self.assertTrue(torrents[3]['seed'] > torrents[4]['seed'])

if __name__ == '__main__':
    unittest.main()
