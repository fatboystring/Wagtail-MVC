from django.template.response import TemplateResponse


def index(request, *args, **kwargs):
    return TemplateResponse(request, 'test_app/index.html', kwargs)


def sub_page(request, *args, **kwargs):
    return TemplateResponse(request, 'test_app/sub_page.html', kwargs)
