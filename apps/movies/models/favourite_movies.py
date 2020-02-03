"""This module contains FavouriteMoviesModel model class."""
from django.db import models

from apps.users.models import CustomUser


class FavouriteMoviesModel(models.Model):
    """Represents favourite movies table."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    imdb_id = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    movie_type = models.CharField(max_length=16)
    poster_url = models.CharField(max_length=512)
    year = models.IntegerField()
