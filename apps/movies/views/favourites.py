"""This module contains FavouritesView class representing favourite movies page."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.movies.models import FavouriteMoviesModel


class FavouritesView(LoginRequiredMixin, ListView):
    """Represents favourite movies list view."""
    template_name = 'movies/favourites.html'
    paginate_by = 10

    def get_queryset(self):
        """Returns user's all favourite movies."""
        return FavouriteMoviesModel.objects.filter(user=self.request.user)
