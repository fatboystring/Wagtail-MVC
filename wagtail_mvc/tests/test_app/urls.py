# -*- coding: utf-8 -*-
"""
URLs for test_app.
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from wagtail_mvc.tests.test_app.views import index, sub_page

urlpatterns = [
    url(r'^sub-page/$', sub_page),
    url(r'^$', index),
]
