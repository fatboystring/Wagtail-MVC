# -*- coding: utf-8 -*-
"""
MVC model mixins for Wagtail CMS
"""
from __future__ import unicode_literals
from django.http import Http404
from django.core.urlresolvers import resolve


class WagtailMvcViewWrapper(object):
    """
    Simple wrapper around a view and corresponding page instance
    that allows the WagtailMvcMixin to return a routable view
    instead of a model with a serve method
    """
    def __init__(self, view, page):
        """
        Sets required attributes of the instance

        :param view: Callable view function
        :param page: Wagtail page model instance
        """
        self.serve = view
        self.page = page

    def get_view_restrictions(self):
        """
        Gets view restrictions from the page instance

        :return: Queryset of PageViewRestriction model instances
        """
        return self.page.get_view_restrictions()


class WagtailMvcMixin(object):
    """
    Model mixin that provides better separation
    between model and view logic for wagtail
    """
    def resolve_view(self, path_components):
        """
        Resolves the view to be rendered

        :param request:
        :param path_components:
        :return:
        """
        if path_components:
            path = '/{0}/'.format('/'.join(path_components))
        else:
            path = '/'
        specific = self.specific
        view, args, kwargs = resolve(path, urlconf=specific.wagtail_url_conf)
        kwargs['page'] = self
        return WagtailMvcViewWrapper(view, self), args, kwargs

    def route(self, request, path_components):
        """
        Custom route method
        Uses wagtails default routing mechanism to get a route result
        then attempts to resolve a view object using the 'wagtail_url_conf'
        attribute on the routed page to get the associated view

        :param request: HttpRequest instance
        :param path_components: List of URL path components

        :return: Iterable containing ViewWrapper|Page, args, kwargs
        """
        try:
            route_result = super(WagtailMvcMixin, self).route(
                request,
                path_components
            )
        except Http404:
            if hasattr(self.specific, 'wagtail_url_conf'):
                return self.resolve_view(path_components)
            else:
                raise
        else:
            if not isinstance(route_result[0], WagtailMvcViewWrapper):
                if hasattr(route_result[0].specific, 'wagtail_url_conf'):
                    return route_result[0].resolve_view(path_components)
            return route_result
