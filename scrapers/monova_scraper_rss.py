import requests
from bs4 import BeautifulSoup
import urllib
from scraper import Scraper
from operator import itemgetter
import time

class MonovaScraperRSS(Scraper):

    def __init__(self):
        Scraper.__init__(self)
        self.site = "monova.com"
    
    def get_torrent_info(self, description):
        torrent_request = requests.get("http://www.monova.org/rss.php?search=" + urllib.quote(description) + "&order=seeds", headers=self.headers)
        torrent_html = torrent_request.text
        torrent_dom = BeautifulSoup(torrent_html)
        torrents = []
        counter = 0
        try:
            #find all torrents
            for torrent in torrent_dom.find_all('item'):
                counter += 1
                if counter < 6: 
                    torrents.append(self.get_torrent_detail(torrent))
        except: 
            #Return an empty object when not data found
            return {}
        return torrents

    def get_torrent_detail(self, torrent):
        try:
        #Obtain the torrent detail
            name = torrent.title.text
            link = torrent.guid.text
            magnet = self.get_torrent_data(link)['magnet']
            description = (torrent.description.text).split()
            seed = int(description[1])
            leech = int(description[3])
            size = description[5] + ' ' + description[6]
            return {'site': self.site, 'name': name, 'link': link,  'magnet': magnet, 'seed': seed, 'leech': leech, 'size': size}
        except:
            return {}

    def get_torrent_data(self, link):
        torrent_data_request = requests.get(link, headers=self.headers)
        torrent_data_html = torrent_data_request.text
        torrent_data_dom = BeautifulSoup(torrent_data_html)
        magnet = torrent_data_dom.find('div', {'id': 'downloadbox'}).find_all('a')[1]['href']
        return {'magnet': magnet}
