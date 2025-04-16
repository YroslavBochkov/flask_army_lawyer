import os
import json
import sys
from flask import Flask, render_template
from flask_frozen import Freezer
from flask_flatpages import pygments_style_defs

app = Flask(__name__)
app.config.from_pyfile('config.py')
freezer = Freezer(app)

def _get_settings():
    with open(app.config['SETTINGS_FILE'], encoding='utf8') as config_file:
        return json.load(config_file)

@app.route("/")
def index():
    settings = _get_settings()
    return render_template('index.html', **settings)

@app.route('/services/')
def services():
    settings = _get_settings()
    return render_template('services.html', **settings)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('monokai'), 200, {'Content-Type': 'text/css'}


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
