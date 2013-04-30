from flask import Flask, render_template
from flask.ext import restful
from kat_scraper import KatScraper

app = Flask(__name__)
api = restful.Api(app)

class Torrent(restful.Resource):
    def get(self, description):
        scraper = KatScraper()
        return scraper.get_torrents(description)

@app.route('/')
def index():
    return render_template('index.html')

api.add_resource(Torrent, '/api/search/<string:description>')

if __name__ == '__main__':
    app.run(debug=True)
