#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.babelex import Babel
from microsite.core.engines import db
from microsite.core import helpers


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://iefschina:iiii@localhost/iefschina'

app.secret_key = '\x94\xabM\x8c\xc8\r_x#\x06\x8ac\x99\xf5/\x83\xe7\xce\x04\x80XVs\xbe'

db.init_app(app)
Babel(app=app, default_locale='zh')

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
app.jinja_env.globals['versioning'] = helpers.versioning

with app.app_context():
    from microsite import views
    from microsite.panel import admin
    from microsite.blueprints import blueprint_www
    admin.init_app(app)

    assert views

    app.register_blueprint(blueprint_www)

    app.add_url_rule('/apps/%s/<path:filename>' %
                        app.name, endpoint='static', #subdomain='static',
                        view_func=app.send_static_file)

