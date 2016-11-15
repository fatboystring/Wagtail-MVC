# -*- coding: utf-8 -*-
"""
MVC model mixins for Wagtail CMS
"""
from __future__ import unicode_literals
from django.http import Http404
from django.core.urlresolvers import resolve
from wagtail.wagtailcore.models import Page, RouteResult


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
        view = WagtailMvcViewWrapper(view, self)
        return RouteResult(view, args, kwargs)

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
        if path_components:
            child_slug = path_components[0]
            remaining_components = path_components[1:]

            try:
                subpage = self.get_children().get(slug=child_slug)
            except Page.DoesNotExist:
                if hasattr(self, 'wagtail_url_conf'):
                    return self.resolve_view(path_components)
                else:
                    raise Http404
            else:
                return subpage.specific.route(request, remaining_components)

        else:
            # request is for this very page
            if self.live:
                if hasattr(self, 'wagtail_url_conf'):
                    return self.resolve_view(path_components)
                else:
                    return RouteResult(self)
            else:
                raise Http404
