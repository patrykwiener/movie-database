"""This module contains HomeView class representing home page."""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Represents home page."""
    template_name = 'movies/home.html'
