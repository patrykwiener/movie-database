# Generated by Django 3.0.2 on 2020-02-03 00:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavouritesMoviesModel',
            new_name='FavouriteMoviesModel',
        ),
    ]
