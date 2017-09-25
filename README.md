[![Wagtail MVC on pypi](https://img.shields.io/badge/pypi-0.2.0-green.svg)](https://pypi.python.org/pypi/wagtail_mvc)
![MIT license](https://img.shields.io/badge/licence-MIT-blue.svg)
![Build status](https://travis-ci.org/fatboystring/Wagtail-MVC.svg?branch=master)

# Wagtail-MVC

A simple app that allows view logic to be written _outside_ of wagtails page model.

## Why?

I enjoy working with wagtail cms but often struggle with the fact that it requires me to write my view logic inside my page models.

In the majority of simple cases this doesn't cause a significant problem.  However, for more complex use cases the approach can lead to circular dependencies, spaghetti code and monolithic model classes.

## Installation

```
pip install wagtail_mvc
```

## Usage

### Models

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

### Urls

A child model of a parent page will often have a url that comprises the parent pages url and the reversed url for the child page.  For child models you may use the `wagtail_mvc_url` decorator from `wagtail_mvc.decorators` to make this easier.

The following implementation example has a parent page whos URL is `/foo/`.  If the call to `reverse` in the example returns the url `/bar/` the decorated function will return `/foo/bar/`.

```
from wagtail_mvc.decorators import wagtail_mvc_url

class MyModel(Page):
    @property
    @wagtail_mvc_url
    def url(self):
        return reverse(
            'my_view_name',
            urlconf='myapp.urls',
            kwargs={'slug': self.slug}
        )
```

## Support

Currently tested against wagtail1.12, watail1.11, wagtail1.10, wagtail1.9, wagtail1.8, wagtail1.7, wagtail1.6 and wagtail1.5 but this package is likely to work with older versions of wagtail without any problems.

# Change Log

 - 0.1.0: Initial creation of the wagtail_mvc app
 - 0.2.0: Added wagtail_mvc_url decorator. Test against wagtail 1.8, 1.9, 1.10, 1.11, 1.12
