# -*- coding: utf-8 -*-
"""
wagtail_mvc decorators
"""
from __future__ import unicode_literals


def wagtail_mvc_url(*decorator_args, **decorator_kwargs):
    """
    Decorates an existing method responsible for generating a url
    prepends the parent url to the generated url to account for

    :param func: The method to decorate
    :return: Full url
    """
    parent_attr = decorator_kwargs.get('parent_attr')

    def decorator(func):
        def outer(self, *args, **kwargs):
            if parent_attr:
                parent = getattr(self, parent_attr, None)
            else:
                parent = self.get_parent()

            parts = parent.url.split('/')
            parts += func(self, *args, **kwargs).split('/')
            return '/{0}/'.format('/'.join([part for part in parts if part]))
        return outer

    if len(decorator_args) == 1 \
            and callable(decorator_args[0]) \
            and not parent_attr:
        # We assume the decorator function has not been called
        # or passed any arguments and return the result of calling
        # the decorator function
        return decorator(decorator_args[0])
    return decorator
