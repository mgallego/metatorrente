import requests
from bs4 import BeautifulSoup
import urllib
from scraper import Scraper
import json


class FenopyScraperApi(Scraper):

    def __init__(self):
        Scraper.__init__(self)
        self.root = 'http://bitsnoop.com'
        self.site = "fenopy.se"
    
    def get_torrent_info(self, description):
        search = "%s" %(description)
        torrent_request = requests.get("http://fenopy.se/module/search/api.php?keyword=" + urllib.quote(search) + "&sort=peer&format=json&limit=10&category=0", headers=self.headers)
        torrents = []
        try:
            for torrent in torrent_request.json():
                torrents.append(self.get_torrent_detail(torrent))
        except: 
            #Return an empty object when not data found
            return {}
        return torrents

    def get_torrent_detail(self, torrent):
        #Obtain the torrent detail
        name = torrent['name']
        link = torrent['page']
        magnet = torrent['magnet']
        seed = int(torrent['seeder'])
        leech = int(torrent['leecher'])
        size = str((int(torrent['size']) / 1024) / 1024) + ' MB'
        return {'site': self.site, 'name': name, 'link': link,  'magnet': magnet, 'seed': seed, 'leech': leech, 'size': size}
