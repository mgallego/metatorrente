import requests
from bs4 import BeautifulSoup
import urllib
from scraper import Scraper
from operator import itemgetter

class KatScraper(Scraper):

    def get_torrent_info(self, description):
        search = "%s" %(description)
        torrent_request = requests.get("http://kat.ph/usearch/" +  urllib.quote(search))
        torrent_html = torrent_request.text
        torrent_dom = BeautifulSoup(torrent_html)
        torrents = []
        try:
            #find all torrents
            for torrent in torrent_dom.find_all('tr', {'class': 'odd'}):
                torrents.append(self.get_torrent_detail(torrent))
            for torrent in torrent_dom.find_all('tr', {'class': 'even'}):
                torrents.append(self.get_torrent_detail(torrent))
        except: 
            #Return an empty object when not data found
            return {}
        return torrents

    def get_torrent_detail(self, torrent):
        #Obtain the torrent detail
        name = torrent.find('div', {'class': 'torrentname'}).find_all('a')[1].text
        magnet = torrent.find('a', {'title': 'Torrent magnet link'})['href']
        seed = int(torrent.find_all('td')[4].text)
        leech = int(torrent.find_all('td')[5].text)
        size = int(torrent.find_all('td')[2].text)
        return {'name': name, 'magnet': magnet, 'seed': seed, 'leech': leech, 'size': size}

    def get_torrents(self, description):
        return sorted(self.get_torrent_info(description), key=itemgetter('seed'), reverse=True)
