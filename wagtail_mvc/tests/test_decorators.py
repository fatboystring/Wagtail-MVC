# -*- coding: utf-8 -*-
"""
wagtail_mvc decorator tests
"""
from __future__ import unicode_literals
from django.test import TestCase
from mock import Mock
from wagtail_mvc.decorators import wagtail_mvc_url


class WagtailMvcUrlDecoratorTestCase(TestCase):
    """
    Tests the wagtail_mvc_url decorator
    """
    def setUp(self):
        """
        Sets up the test case
        """
        super(WagtailMvcUrlDecoratorTestCase, self).setUp()
        self.parent = Mock()
        self.parent.url = '/base/'
        self.instance = Mock()
        self.instance.get_parent = Mock(return_value=self.parent)

    def test_generates_correct_url(self):
        """
        The decorator should generate the correct url
        """
        func = wagtail_mvc_url(Mock(return_value='/foo/bar/'))
        self.assertEqual(func(self.instance), '/base/foo/bar/')

    def test_generates_correct_url_2(self):
        """
        The decorator should generate the correct url
        """
        func = wagtail_mvc_url(Mock(return_value='foo/bar'))
        self.assertEqual(func(self.instance), '/base/foo/bar/')

    def test_generates_correct_url_3(self):
        """
        The decorator should generate the correct url
        """
        self.parent.url = 'base'
        func = wagtail_mvc_url(Mock(return_value='foo/bar'))
        self.assertEqual(func(self.instance), '/base/foo/bar/')
