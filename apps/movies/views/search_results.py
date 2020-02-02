from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.views.generic import TemplateView, ListView

from apps.movies.services.omdb_api import OMDBApi


class SearchResultsView(LoginRequiredMixin, ListView):
    template_name = 'movies/search_results.html'
    paginate_by = 2

    def search_for_movies(self, title):
        client = OMDBApi('da952bfb')
        self.queryset = client.search_all_movies(title)

    def get(self, request, *args, **kwargs):
        title = request.GET.get('t')
        if title is None:
            return HttpResponseNotFound()
        self.search_for_movies(title)
        return super().get(request, *args, **kwargs)
