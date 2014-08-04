# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from flask import request, views, render_template
from microsite.blueprints import blueprint_www


from microsite.models import ChannelModel, ArticleModel


class IndexView(views.MethodView):
    '''
        首页
    '''

    def get(self):
        lang = request.args.get('lang', None)
        # 根据频道语言划分
        channels = ChannelModel.query.all()
        if lang=='en':
            channels = filter(lambda x: re.match(r'[a-zA-Z\b]+', x.name), channels)
        else:
            channels = filter(lambda x: not re.match(r'[a-zA-Z\b]+', x.name), channels)
            
        return render_template('www/index.html', channels=channels)


blueprint_www.add_url_rule('/', view_func=IndexView.as_view(b'index'),
                                endpoint='index', methods=['GET'])

