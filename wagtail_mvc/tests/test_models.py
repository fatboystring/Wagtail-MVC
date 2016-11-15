# -*- coding: utf-8 -*-
"""
wagtail_mvc tests
"""
from __future__ import unicode_literals

from django.http import Http404
from django.test import RequestFactory, TestCase
from mock import Mock
from wagtail.wagtailcore.models import RouteResult

from wagtail_mvc.models import WagtailMvcViewWrapper
from wagtail_mvc.tests.test_app.factories import (
    TestModelOneFactory,
    TestModelTwoFactory
)


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
    def setUp(self):
        super(WagtailMvcMixinTestCase, self).setUp()
        self.request = RequestFactory().get('/fake-path/')
        self.homepage = TestModelOneFactory.create(
            path="0002",
            depth=0,
            url_path="/",
            numchild=1
        )
        self.page_1 = TestModelTwoFactory.create(path="00020001", depth=1)

    def test_renders_if_wagtail_url_conf_not_defined(self):
        """
        The page should render if no wagtail_url_conf attribute is defined
        """
        response = self.homepage.route(self.request, [])
        self.assertIsInstance(response, RouteResult)
        self.assertEqual(response[0], self.homepage)

    def test_resolve_view_resolves_view(self):
        """
        The resolve_view method should return the correct data
        """
        response = self.page_1.route(self.request, [])
        self.assertIsInstance(response, RouteResult)
        self.assertIsInstance(response[0], WagtailMvcViewWrapper)
        self.assertTrue(callable(response[0].serve))
        self.assertEqual(response[0].page, self.page_1)
        self.assertEqual(response[1], [])
        self.assertEqual(response[2], {'page': self.page_1})

    def test_resolve_view_raises_404(self):
        """
        The resolve_view method should raise a Resolver404 exception
        """
        self.assertRaises(Http404, self.page_1.route, self.request, ['foo'])

    def test_url_config_used_to_serve_sub_page(self):
        """
        The url config should be used to serve a sub page
        """
        response = self.page_1.route(self.request, ['sub-page'])
        self.assertIsInstance(response, RouteResult)
        self.assertIsInstance(response[0], WagtailMvcViewWrapper)
        self.assertTrue(callable(response[0].serve))
        self.assertEqual(response[0].page, self.page_1)
        self.assertEqual(response[1], [])
        self.assertEqual(response[2], {'page': self.page_1})
