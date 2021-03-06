# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from wtforms.widgets import TextArea
from wtforms import TextAreaField, validators
from flask.ext.admin.contrib.sqla import ModelView
from studio.core.engines import db

from microsite.models import ArticleModel


class CKTextAreaWidget(TextArea):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):

    widget = CKTextAreaWidget()


class Article(ModelView):

    create_template = 'panel/article_edit.html'
    edit_template = 'panel/article_edit.html'
    column_labels = {'id': 'ID',
                     'title': '标题',
                     'is_sticky': '置顶',
                     'channel': '频道',
                     'date_published': '发布时间',
                     'date_created': '创建时间'}
    column_list = ['id', 'channel',  'is_sticky', 'title', 'date_published', 'date_created']
    column_searchable_list = ['title', ]
    column_default_sort = ('date_published', True)
    form_extra_fields = {
        'content': CKTextAreaField('内容', validators=[validators.Required()]),
    }

    def __init__(self, **kwargs):
        super(Article, self).__init__(ArticleModel, db.session, **kwargs)

    def create_form(self, obj=None):
        form = super(Article, self).create_form()
        delattr(form, 'cid')
        delattr(form, 'date_created')
        return form

    def edit_form(self, obj=None):
        form = super(Article, self).edit_form(obj=obj)
        delattr(form, 'cid')
        delattr(form, 'date_created')
        return form
