# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask.ext.admin.contrib.sqla import ModelView
from studio.core.engines import db
from microsite.models import ChannelModel


class Channel(ModelView):

    column_labels = {'name': '名称', 'introduction': '简介'}

    def __init__(self, **kwargs):
        super(Channel, self).__init__(ChannelModel, db.session, **kwargs)

    def create_form(self, obj=None):
        form = super(Channel, self).create_form()
        delattr(form, 'articles')
        delattr(form, 'all_articles')
        return form

    def edit_form(self, obj=None):
        form = super(Channel, self).edit_form()
        delattr(form, 'articles')
        delattr(form, 'all_articles')
        return form
