import json
from functools import wraps
from flask import Flask, render_template, redirect, request, current_app, jsonify
from flask.ext import restful
from scrapers.scrap_all import ScrapAll

app = Flask(__name__)
api = restful.Api(app)


def jsonp(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)
    return decorated_function

class Torrent(restful.Resource):
    @jsonp
    def get(self, description):
        scraper = ScrapAll()
        return jsonify({'result': scraper.get_torrents(description)})

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
