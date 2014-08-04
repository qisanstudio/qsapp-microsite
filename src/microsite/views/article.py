# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from flask import views, render_template
from microsite.blueprints import blueprint_www


from microsite.models import ChannelModel, ArticleModel


class ArticleView(views.MethodView):
    '''
        文章页
    '''

    def get(self, aid):
        channels = ChannelModel.query.all()
        article = ArticleModel.query.get(aid)
        if re.match(r'[a-zA-Z\b]+', article.channel.name):
            channels = filter(lambda x: re.match(r'[a-zA-Z\b]+', x.name), channels)
        else:
            channels = filter(lambda x: not re.match(r'[a-zA-Z\b]+', x.name), channels)
        return render_template('www/article.html', channels=channels, article=article)


blueprint_www.add_url_rule('/article/<int:aid>/', view_func=ArticleView.as_view(b'article'),
                                endpoint='article', methods=['GET'])

