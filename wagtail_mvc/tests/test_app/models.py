# -*- coding: utf-8 -*-
"""
Test app models for the wagtail_mvc app
"""
from __future__ import unicode_literals
from wagtail.wagtailcore.models import Page
from wagtail_mvc.models import WagtailMvcMixin


class TestModelOne(WagtailMvcMixin, Page):
    """
    Test model with no wagtail_url_conf attribute
    """


class TestModelTwo(WagtailMvcMixin, Page):
    """
    Test model with wagtail_url_conf attribute
    """
    wagtail_url_conf = 'wagtail_mvc.tests.test_app.urls'
