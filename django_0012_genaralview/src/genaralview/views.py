from _ast import Str

from django.views.generic.base import TemplateView
class HomePageView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['content'] = "AAAAAAAAAAAAAAAAAAAAAAA"
        return context