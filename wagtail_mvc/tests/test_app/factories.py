# -*- coding: utf-8 -*-
"""
Test app factories for the wagtail_mvc app
"""
from __future__ import unicode_literals

import factory

from wagtail_mvc.tests.test_app.models import TestModelOne, TestModelTwo


class TestModelOneFactory(factory.DjangoModelFactory):
    """
    Factory for generating TestModelOne instances
    """
    title = factory.Sequence(lambda x: 'test page one {0}'.format(x))
    depth = 0

    class Meta(object):
        """
        FactoryBoy properties
        """
        model = TestModelOne


class TestModelTwoFactory(factory.DjangoModelFactory):
    """
    Factory for generating TestModelTwo instances
    """
    title = factory.Sequence(lambda x: 'test page two {0}'.format(x))
    depth = 0

    class Meta(object):
        """
        FactoryBoy properties
        """
        model = TestModelTwo
