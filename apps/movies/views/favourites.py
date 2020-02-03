from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.movies.models import FavouritesMoviesModel


class FavouritesView(LoginRequiredMixin, ListView):
    template_name = 'movies/favourites.html'

    def get_queryset(self):
        return FavouritesMoviesModel.objects.filter(user=self.request.user)
