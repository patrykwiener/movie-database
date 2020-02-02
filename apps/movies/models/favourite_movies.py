from django.db import models

from apps.users.models import CustomUser


class FavouritesMoviesModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    imdb_id = models.CharField(max_length=128)
