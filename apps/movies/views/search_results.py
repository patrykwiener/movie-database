"""This module contains SearchResultsView class representing search for movies view."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.views.generic import ListView

from apps.movies.models import FavouriteMoviesModel
from apps.movies.services.omdb_api import client


class SearchResultsView(LoginRequiredMixin, ListView):
    """Represents search for movies class view."""
    template_name = 'movies/search_results.html'
    paginate_by = 10

    def search_for_movies(self, title):
        """Sets queryset with search by title movies derived from OMDb Api service."""
        self.queryset = client.search_all_movies(title)

    def set_extra_context(self, title):
        """Sets page extra context. Adds list of favourites ids."""
        favourites_imdb_id = [movie.imdb_id for movie in FavouriteMoviesModel.objects.filter(user=self.request.user)]
        self.extra_context = {
            'title': title,
            'favourites': favourites_imdb_id,
        }

    def get(self, request, *args, **kwargs):
        """Handles GET request. Searches for movies and sets extra context."""
        title = request.GET.get('t')
        if title is None:
            return HttpResponseNotFound()

        self.search_for_movies(title)
        self.set_extra_context(title)
        return super().get(request, *args, **kwargs)
