from wagtail.wagtailcore.models import Page
from wagtail_mvc.models import WagtailMvcMixin


class TestModelOne(WagtailMvcMixin, Page):
    """
    Test model with no wagtail_url_conf attribute
    """


class TestModelTwo(WagtailMvcMixin, Page):
    """
    Test model with wagtail_url_conf attribute
    """
    wagtail_url_conf = 'test_app.urls'