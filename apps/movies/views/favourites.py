from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from apps.movies.models import FavouriteMoviesModel


class FavouritesView(LoginRequiredMixin, ListView):
    template_name = 'movies/favourites.html'
    paginate_by = 10

    def get_queryset(self):
        return FavouriteMoviesModel.objects.filter(user=self.request.user)
