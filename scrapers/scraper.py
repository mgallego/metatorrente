from operator import itemgetter

class Scraper(object):

    def __init__(self):
        self.headers = {'User-agent': 'Mozilla/5.0'}

    def get_torrents(self, description):
        return self.get_torrent_info(description)

    @staticmethod
    def sort(torrents, field):
        return sorted(torrents, key=itemgetter(field), reverse=True)            

    def return_null_torrent(self):
        return {'site': '', 'name': '', 'link': '',  'magnet': '', 'seed': 0, 'leech': 0, 'size': ''}
