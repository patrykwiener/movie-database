from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from apps.movies.models import FavouriteMoviesModel


class DeleteFromFavouritesView(LoginRequiredMixin, DeleteView):
    template_name = 'movies/delete_favourite.html'
    model = FavouriteMoviesModel
    success_url = reverse_lazy('movies:favourites')

    def get_object(self, queryset=None):
        """Returns FavouriteMoviesModel object to delete found by URL pk."""
        pk = self.kwargs.get('pk')
        return get_object_or_404(self.model, user=self.request.user, id=pk)
