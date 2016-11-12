# -*- coding: utf-8 -*-
"""
wagtail_mvc tests
"""
from __future__ import unicode_literals
from django.test import TestCase
from mock import Mock
from wagtail.wagtailcore.models import Site
from test_app.factories import TestModelOneFactory, TestModelTwoFactory
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
    def setUp(self):
        super(WagtailMvcMixinTestCase, self).setUp()
        self.homepage = TestModelOneFactory.create(path="0002", depth=0, url_path="/", numchild=1)
        self.page_1 = TestModelTwoFactory.create(path="00020001", depth=1)
        self.site = Site.objects.create(hostname='example.com', root_page=self.homepage, is_default_site=True)

    def test_renders_if_wagtail_url_conf_not_defined(self):
        """
        The page should render if no wagtail_url_conf attribute is defined
        """
        response = self.client.get(self.homepage.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'test_app/test_model_one.html')

    def test_resolve_view_resolves_view(self):
        """
        The resolve_view method should return the correct data
        """
        response = self.client.get(self.page_1.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'test_app/index.html')

    def test_page_in_view_kwargs(self):
        """
        The resolve_view method should add the page instance to the view kwargs
        """
        response = self.client.get(self.page_1.url)
        self.assertEqual(response.context['page'], self.page_1)

    def test_resolve_view_raises_404(self):
        """
        The resolve_view method should raise a Resolver404 exception
        """
        response = self.client.get('{0}foo/'.format(self.page_1.url))
        self.assertEqual(response.status_code, 404)

    def test_url_config_used_to_serve_sub_page(self):
        """
        The defined url config should be used to serve a sub page when a partial url is matched
        """
        response = self.client.get('{0}sub-page/'.format(self.page_1.url))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'test_app/sub_page.html')
