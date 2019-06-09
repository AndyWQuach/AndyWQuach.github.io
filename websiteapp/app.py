# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.scss import Scss
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
Scss(app, static_dir='static', asset_dir='sass')

app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)
