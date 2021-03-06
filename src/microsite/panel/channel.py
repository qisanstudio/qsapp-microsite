# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import flash
from flask.ext.admin.contrib.sqla import ModelView
from studio.core.engines import db
from microsite.models import ChannelModel, ArticleModel


class Channel(ModelView):

    column_labels = {'name': '名称', 'introduction': '简介'}

    def __init__(self, **kwargs):
        super(Channel, self).__init__(ChannelModel, db.session, **kwargs)

    def delete_model(self, model):
        if ArticleModel.query.filter_by(cid=model.id).count() > 0:
            flash('有文章关联，不能删除!')
            return False
        return super(Channel, self).delete_model(model)

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
