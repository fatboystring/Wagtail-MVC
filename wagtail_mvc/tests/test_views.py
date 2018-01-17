from mock import Mock, patch
from django.test import RequestFactory, TestCase

from wagtail_mvc.views import WagtailMvcView


class WagtailMvcViewTestCase(TestCase):
    """
    Tests the WagtailMvcView
    """
    @classmethod
    def setUpTestData(cls):
        cls.page = Mock()
        cls.page.get_context = Mock()
        cls.page.get_template = Mock(return_value='foo/bar/baz.html')

        cls.request = RequestFactory().get('/fake-path/')

        cls.view = WagtailMvcView()
        cls.view.request = cls.request
        cls.view.args = ('foo', 'bar',)
        cls.view.kwargs = dict(a='b', c='d')
        cls.view.page = cls.page

    def test_dispatch_raises_key_error(self):
        """
        dispatch method should raise a KeyError if the page instance is missing
        """
        self.assertRaises(KeyError, self.view.dispatch, self.request)

    def test_dispatch_not_raises_key_error(self):
        """
        dispatch method should raise a KeyError if the page instance is missing
        """
        with patch.object(self.view, 'get_context_data') as patched:
            patched.return_value = {}
            self.view.dispatch(self.request, page=self.page)

    def test_get_template_names(self):
        """
        Should return the expected template names
        """
        self.assertListEqual(
            self.view.get_template_names(),
            ['foo/bar/baz.html']
        )

    def test_get_object(self):
        """
        Should return the page object
        """
        self.assertEqual(
            self.view.get_object(),
            self.page
        )
