"""This module contains movies app url definitions."""
from django.urls import path

from apps.movies.views.add_to_favourites import AddToFavouritesView
from apps.movies.views.home import HomeView
from apps.movies.views.search_results import SearchResultsView

app_name = 'movies'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('add-favourites/', AddToFavouritesView.as_view(), name='add_to_favourites')
]
