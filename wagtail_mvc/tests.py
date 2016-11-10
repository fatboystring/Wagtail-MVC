# -*- coding: utf-8 -*-
"""
wagtail_mvc tests
"""
from __future__ import unicode_literals
from django.test import TestCase
from mock import Mock
from wagtail_mvc.models import WagtailMvcViewWrapper


class WagtailMvcViewWrapperTestCase(TestCase):
    """
    Tests the WagtailMvcViewWrapper
    """
    def setUp(self):
        super(WagtailMvcViewWrapperTestCase, self).setUp()
        self.view = Mock()
        self.page = Mock(methods=['get_view_restrictions'])
        self.instance = WagtailMvcViewWrapper(self.view, self.page)

    def test_serve_calls_view(self):
        """
        The instances serve attribute should call the view
        """
        self.instance.serve()
        self.view.assert_called_with()

    def test_get_view_restrictions(self):
        """
        The method should call the get_view_restrictions method on the page
        """
        self.instance.get_view_restrictions()
        self.page.get_view_restrictions.assert_called_with()


class WagtailMvcMixinTestCase(TestCase):
    """
    Tests the WagtailMvcMixin
    """
    def test_calls_serve_if_wagtail_url_conf_not_defined(self):
        """
        The serve method should still be called if the wagtail_url_conf attribute is not defined
        """
        pass

    def test_resolve_view_resolves_view(self):
        """
        The resolve_view method should return the correct data
        """
        pass

    def test_page_in_view_kwargs(self):
        """
        The resolve_view method should add the page instance to the view kwargs
        """
        pass

    def test_resolve_view_raises_404(self):
        """
        The resolve_view method should raise a Resolver404 exception
        """
        pass

    def test_url_config_used_to_serve_actual_page(self):
        """
        The defined url config should be used to serve the page when a full url is matched
        """
        pass

    def test_url_config_used_to_serve_sub_page(self):
        """
        The defined url config should be used to serve a sub page when a partial url is matched
        """
        pass
