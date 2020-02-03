"""This module contains movies app url definitions."""
from django.urls import path, re_path

from apps.movies.views.add_to_favourites import AddToFavouritesView
from apps.movies.views.delete_from_favourites import DeleteFromFavouritesView
from apps.movies.views.favourites import FavouritesView
from apps.movies.views.home import HomeView
from apps.movies.views.search_results import SearchResultsView

app_name = 'movies'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('favourites/', FavouritesView.as_view(), name='favourites'),
    path('add-favourites/', AddToFavouritesView.as_view(), name='add_to_favourites'),
    re_path(r'^delete-favourite/(?P<pk>\w+)/$', DeleteFromFavouritesView.as_view(), name='delete_favourite'),
]
