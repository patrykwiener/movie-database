from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.views.generic import ListView

from apps.movies.services.omdb_api import client


class SearchResultsView(LoginRequiredMixin, ListView):
    template_name = 'movies/search_results.html'
    paginate_by = 10

    def search_for_movies(self, title):
        self.queryset = client.search_all_movies(title)

    def get(self, request, *args, **kwargs):
        title = request.GET.get('t')
        if title is None:
            return HttpResponseNotFound()

        self.extra_context = {
            'title': title
        }

        self.search_for_movies(title)
        return super().get(request, *args, **kwargs)