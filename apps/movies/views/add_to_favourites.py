import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View

from apps.movies.models import FavouriteMoviesModel


class AddToFavouritesView(LoginRequiredMixin, View):

    def get(self, request):
        imdb_id = request.GET['imdb_id']
        title = request.GET['title']
        movie_type = request.GET['type']
        poster_url = request.GET['poster']
        year = int(request.GET['year'])

        if not imdb_id:
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
