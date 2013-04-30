from flask import Flask
from flask.ext import restful
from kat_scraper import KatScraper

app = Flask(__name__)
api = restful.Api(app)

class Torrent(restful.Resource):
    def get(self, description):
        scraper = KatScraper()
        return scraper.get_torrents(description)

api.add_resource(Torrent, '/api/search/<string:description>')

if __name__ == '__main__':
    app.run(debug=True)
