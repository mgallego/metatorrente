import requests
from bs4 import BeautifulSoup
import urllib
from scraper import Scraper
from operator import itemgetter
import time

class BSScraperRSS(Scraper):

    def __init__(self):
        Scraper.__init__(self)
        self.root = 'http://bitsnoop.com'
        self.site = "bitsnoop.com"
    
    def get_torrent_info(self, description):
        search = "%s" %(description)
        torrent_request = requests.get("http://bitsnoop.com/search/all/" +  urllib.quote(search) + "/c/d/1/?fmt=rss", headers=self.headers)
        torrent_html = torrent_request.text
        torrent_dom = BeautifulSoup(torrent_html)
        torrents = []
        try:
            #find all torrents
            for torrent in torrent_dom.find_all('item'):
                torrents.append(self.get_torrent_detail(torrent))
        except: 
            #Return an empty object when not data found
            return {}
        return torrents

    def get_torrent_detail(self, torrent):
        #Obtain the torrent detail
        name = torrent.title.text
        link = torrent.link.text
        magnet = torrent.torrent.magneturi.text
        seed = int(torrent.numseeders.text)
        leech = int(torrent.numleechers.text)
        size = str((int(torrent.size.text) / 1024) / 1024) + ' MB'
        return {'site': self.site, 'name': name, 'link': link,  'magnet': magnet, 'seed': seed, 'leech': leech, 'size': size}
