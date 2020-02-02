from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class SearchResultsView(LoginRequiredMixin, TemplateView):
    template_name = 'movies/search_results.html'
