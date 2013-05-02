import requests
from bs4 import BeautifulSoup
import urllib
from scraper import Scraper

class KatScraperRSS(Scraper):

    def __init__(self):
        Scraper.__init__(self)
        self.root = 'http://kat.ph'
        self.site = "kat.ph"
    
    def get_torrent_info(self, description):
        search = "%s" %(description)
        torrent_request = requests.get("http://kat.ph/usearch/" +  urllib.quote(search) + '/?field=seeders&sorder=desc&rss=1', headers=self.headers)
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
        magnet = torrent.find('torrent:magneturi').text
        seed = int(torrent.find('torrent:seeds').text)
        leech = int(torrent.find('torrent:peers').text) - seed
        size = str((int(torrent.find('torrent:contentlength').text) / 1024) / 1024) + ' MB'
        return {'site': self.site, 'name': name, 'link': link,  'magnet': magnet, 'seed': seed, 'leech': leech, 'size': size}
