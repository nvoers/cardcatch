from django.views.generic import TemplateView
from django.shortcuts import render


class IndexView(TemplateView):
    """Index view."""

    template_name = "base.html"

    def get(self, request, **kwargs):
        """
        GET request for IndexView.

        :param request: the request
        :param kwargs: keyword arguments
        :return: a render of the index page
        """
        return render(request, self.template_name)
