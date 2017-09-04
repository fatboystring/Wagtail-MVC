# -*- coding: utf-8 -*-
"""
wagtail_mvc decorators
"""
from __future__ import unicode_literals


def wagtail_mvc_url(func):
    """
    Decorates an existing method responsible for generating a url
    prepends the parent url to the generated url to account for

    :param func: The method to decorate
    :return: Full url
    """
    def outer(self, *args, **kwargs):
        parts = self.get_parent().url.split('/')
        parts += func(self, *args, **kwargs).split('/')
        return '/{0}/'.format('/'.join([part for part in parts if part]))
    return outer
