# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from flask import request, views, render_template
from flask.ext.paginate import Pagination
from microsite.blueprints import blueprint_www


from microsite.models import ChannelModel


class ChannelView(views.MethodView):
    '''
        首页
    '''
    
    @property
    def page(self):
        try:
            return int(request.args.get('page', 1))
        except ValueError:
            return 1

    def get(self, cid):
        channels = ChannelModel.query.all()
        channel = ChannelModel.query.get(cid)

        if re.match(r'[a-zA-Z\b]+', channel.name):
            channels = filter(lambda x: re.match(r'[a-zA-Z\b]+', x.name), channels)
        else:
            channels = filter(lambda x: not re.match(r'[a-zA-Z\b]+', x.name), channels)
        
        pagination = Pagination(bs_version=3, page=self.page, total=channel.articles.count())
        return render_template('www/channel.html', 
                                channels=channels, 
                                channel=channel,
                                pagination=pagination)


blueprint_www.add_url_rule('/channel/<int:cid>/', view_func=ChannelView.as_view(b'channel'),
                                endpoint='channel', methods=['GET'])
