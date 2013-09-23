import json
from functools import wraps
from flask import Flask, render_template, redirect, request, current_app, jsonify
from flask.ext import restful
from scrapers.scrap_all import ScrapAll

app = Flask(__name__)
api = restful.Api(app)


def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f().data) + ')'
            return current_app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)
    return decorated_function

class Torrent(restful.Resource):
    @support_jsonp
    def get(self, description):
        scraper = ScrapAll()
        return scraper.get_torrents(description)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api_doc():
    return render_template('api.html')

@app.route('/about')
def about():
    return render_template('about.html')

api.add_resource(Torrent, '/api/torrents/<string:description>')

if __name__ == '__main__':
    app.run(debug=True)
