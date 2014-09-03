#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.babelex import Babel
from studio.core.flask.app import StudioFlask
from studio.core.engines import db


app = StudioFlask(__name__)

db.init_app(app)
Babel(app=app, default_locale='zh')


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

