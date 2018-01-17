from django.views.generic import DetailView


class WagtailMvcView(DetailView):
    """
    Basic default wagtail mvc view class
    """
    page = None

    def dispatch(self, request, *args, **kwargs):
        """
        Pops the page out of the keyword args and
        stores it against the view instance

        :param request: HttpRequest instance
        :param args: Default positional args
        :param kwargs: Default keyword args

        :return: HttpResponse
        """
        self.page = kwargs.pop('page')
        return super(WagtailMvcView, self).dispatch(request, *args, **kwargs)

    def get_template_names(self):
        """
        Returns a list of potential template
        names for the view

        :return: List containing the pages own template
        """
        return [self.page.get_template(
            self.request,
            *self.args,
            **self.kwargs
        )]

    def get_object(self):
        """
        We return the page instance by default

        :return: wagtail page model instance
        """
        return self.page

    def get_context_data(self, **kwargs):
        """
        Adds the pages own context data to the view context data

        :param kwargs: Default keyword args
        :return: Dict of template data
        """
        ctx = super(WagtailMvcView, self).get_context_data(**kwargs)
        ctx.update(self.page.get_context(
            self.request,
            *self.args,
            **kwargs
        ))
        return ctx
