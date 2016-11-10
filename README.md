# Wagtail-MVC

A simple app that allows view logic to be written _outside_ of wagtails page model.

## Why?

I enjoy working with wagtail cms but often struggle with the fact that it requires me to write my view logic inside my page models.

In the majority of simple cases this doesn't cause a significant problem.  However, for more complex use cases the approach can lead to circular dependencies, spaghetti code and monolithic model classes.

## Installation

Release to PyPi coming soon!

## Usage

Just mix the `WagtailMvcMixin` class into your page model and define a `wagtail_url_conf` attribute on your model.

Example:

```
from wagtail.wagtailcore.models import Page
from wagtail_mvc.models import WagtailMvcMixin


class MyPage(WagtailMvcMixin, Page):
    wagtail_url_conf = 'my_app.urls'
    ....
```

The example above will resolve the appropriate view from the `urls.py` file at `my_app/urls.py`.

For example:

Consider the page shown in the example above being available in the page tree at `/foo/bar/`.
When a user makes a request for `/foo/bar/` the remaining (unmatched) part of the path (along with the defined url_conf) is passed to django's resolve method.

So:

A request for `/foo/bar/` would call `resolve('', url_config='my_app.urls')`
A request for `/foo/bar/baz/` would call `resolve('baz/', url_config='my_app.urls')`

If a view could not be resolved for whatever reason a standard 404 will be raised and returned.

## Support

Currently tested against wagtail1.7 but this package is likely to work with older versions of wagtail without any problems.  Tests coming soon.

# Change Log

 - 0.1.0: Initial creation of the wagtail_mvc app
