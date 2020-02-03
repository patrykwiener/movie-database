"""This module contains AddToFavouritesView class handling adding and removing from favourites."""
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View

from apps.movies.models import FavouriteMoviesModel


class AddToFavouritesView(LoginRequiredMixin, View):
    """Adds or removes favourites movies."""

    def get_request_param(self, param: str):
        """Gets param form request."""
        return self.request[param]

    def get(self, request):
        """Handles GET request. Adds movie to favourites or when its already in database, removes it."""
        imdb_id = self.get_request_param('imdb_id')
        title = self.get_request_param('title')
        movie_type = self.get_request_param('type')
        poster_url = self.get_request_param('poster')
        year = self.get_request_param('year')

        if not imdb_id or not title or not movie_type or not poster_url or not year:
            return HttpResponse(json.dumps({
                "added_to_favourites": False
            }))

        movie_queryset = FavouriteMoviesModel.objects.filter(user=request.user, imdb_id=imdb_id)
        if movie_queryset.exists():
            movie_queryset.delete()
        else:
            FavouriteMoviesModel.objects.create(
                user=request.user,
                imdb_id=imdb_id,
                title=title,
                movie_type=movie_type,
                poster_url=poster_url,
                year=year
            )

        return HttpResponse(json.dumps({
            "added_to_favourites": True
        }))
