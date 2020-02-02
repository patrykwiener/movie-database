from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.views.generic import ListView

from apps.movies.models import FavouritesMoviesModel
from apps.movies.services.omdb_api import client


class SearchResultsView(LoginRequiredMixin, ListView):
    template_name = 'movies/search_results.html'
    paginate_by = 10

    def search_for_movies(self, title):
        self.queryset = client.search_all_movies(title)
        # self.queryset = [1]

    def set_extra_context(self, title):
        favourites_imdb_id = [movie.imdb_id for movie in FavouritesMoviesModel.objects.filter(user=self.request.user)]
        self.extra_context = {
            'title': title,
            'favourites': favourites_imdb_id,
        }

    def get(self, request, *args, **kwargs):
        title = request.GET.get('t')
        if title is None:
            return HttpResponseNotFound()

        self.search_for_movies(title)
        self.set_extra_context(title)
        return super().get(request, *args, **kwargs)
