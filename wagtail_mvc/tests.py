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
