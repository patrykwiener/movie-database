import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View

from apps.movies.models import FavouritesMoviesModel


class AddToFavouritesView(LoginRequiredMixin, View):

    def get(self, request):
        imdb_id = request.GET['imdb_id']
        if not imdb_id:
            return HttpResponse(json.dumps({
                "added_to_favourites": False
            }))

        movie_queryset = FavouritesMoviesModel.objects.filter(user=request.user, imdb_id=imdb_id)
        if movie_queryset.exists():
            movie_queryset.delete()
        else:
            FavouritesMoviesModel.objects.create(user=request.user, imdb_id=imdb_id)

        return HttpResponse(json.dumps({
            "added_to_favourites": True
        }))
