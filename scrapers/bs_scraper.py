import requests
from bs4 import BeautifulSoup
import urllib
from scraper import Scraper
from operator import itemgetter

class BSScraper(Scraper):

    def __init__(self):
        Scraper.__init__(self)
        self.root = 'http://bitsnoop.com'
        self.site = "bitsnoop.com"
    
    def get_torrent_info(self, description):
        search = "%s/c/d/1" %(description)
        torrent_request = requests.get("http://bitsnoop.com/search/all/" +  urllib.quote(search), headers=self.headers)
        torrent_html = torrent_request.text
        torrent_dom = BeautifulSoup(torrent_html)
        torrents = []
        try:
            #find all torrents
            for torrent in torrent_dom.find('ol', {'id': 'torrents'}).find_all('li'):
                torrents.append(self.get_torrent_detail(torrent))
        except: 
            #Return an empty object when not data found
            return {}
        return torrents

    def get_torrent_detail(self, torrent):
        #Obtain the torrent detail
        name = torrent.find('a').text
        link = self.root + torrent.find('a')['href']
        magnet = self.get_torrent_data(link)['magnet']
        seed = int((torrent.find('div', {'class': 'torInfo'}).find('span', {'class': 'seeders'}).text).replace(',',''))
        leech = int((torrent.find('div', {'class': 'torInfo'}).find('span', {'class': 'leechers'}).text).replace(',',''))
        size = (torrent.find('div', {'id': 'sz'}).find('td').text).replace(torrent.find('div', {'id': 'sz'}).find('td').div.text,'')
        return {'site': self.site, 'name': name, 'link': link,  'magnet': magnet, 'seed': seed, 'leech': leech, 'size': size}

    def get_torrent_data(self, link):
        torrent_data_request = requests.get(link, headers=self.headers)
        torrent_data_html = torrent_data_request.text
        torrent_data_dom = BeautifulSoup(torrent_data_html)
        magnet = torrent_data_dom.find('a', {'title': 'Magnet Link'})['href']
        return {'magnet': magnet}
