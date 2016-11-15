# -*- coding: utf-8 -*-
"""
Test app views for the wagtail_mvc app
"""
from __future__ import unicode_literals
from django.template.response import TemplateResponse


def index(request, *args, **kwargs):
    """
    Index view

    :param request: Request instance
    :param args: Default positional args
    :param kwargs: Default keyword args

    :return: TemplateResponse instance
    """
    return TemplateResponse(request, 'test_app/index.html', kwargs)


def sub_page(request, *args, **kwargs):
    """
    Sub Page view

    :param request: Request instance
    :param args: Default positional args
    :param kwargs: Default keyword args

    :return: TemplateResponse instance
    """
    return TemplateResponse(request, 'test_app/sub_page.html', kwargs)
