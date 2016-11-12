from test_app.models import TestModelOne, TestModelTwo
import factory


class TestModelOneFactory(factory.DjangoModelFactory):

    title = factory.Sequence(lambda x: 'test page one {0}'.format(x))
    depth = 0

    class Meta(object):
        model = TestModelOne


class TestModelTwoFactory(factory.DjangoModelFactory):

    title = factory.Sequence(lambda x: 'test page two {0}'.format(x))
    depth = 0

    class Meta(object):
        model = TestModelTwo
