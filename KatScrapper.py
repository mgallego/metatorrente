import requests
from bs4 import BeautifulSoup
import urllib

class KatScraper():

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
        torrent_title = torrent.find('div', {'class': 'torrentname'}).find_all('a')[1].text
        magnet_link = torrent.find('a', {'title': 'Torrent magnet link'})['href']
        seed = torrent.find_all('td')[4].text
        leech = torrent.find_all('td')[5].text
        return {'torrent_title': torrent_title, 'magnet_link': magnet_link, 'seed': seed, 'leech': leech}

scraper = KatScraper()
print scraper.get_torrent_info('game')
