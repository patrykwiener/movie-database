"""This module contains OMDBApi class representing OMDbApi service wrapper."""
import re
from collections import namedtuple
from typing import List

import requests


class OMDBApi:
    """
    This class wraps OMDbApi.
    """

    URL = 'http://www.omdbapi.com'

    def __init__(self, api_key):
        """Requires OMDbApi key."""
        self._api_key = api_key
        self._session = requests.Session()

    def search_all_movies(self, title: str) -> List[object]:
        """
        Searches for all movies specified by the given title. Because of OMDbApi constraints, to return all movies
        multiple requests have to be send. The method gathers results from all requests and returns all of them.

        :param title: searched movie title
        :return: all movies corresponding to the given title
        """
        all_movies = []
        for page in range(100):
            current_movie_page = self.search_movies(title, page)
            all_movies.extend(current_movie_page)
            if len(current_movie_page) < 10:
                return all_movies

    def search_movies(self, title: str, page: int) -> List[object]:
        """
        Searches for movies by title. Additionally requires number of searching page, because OMDbApi response results
        are divided into pages. The maximum number of movies in a single response is 10 total.

        :param title: movie title
        :param page: currently searched movie page number
        :return: list of movie objects
        """
        params = {
            'apikey': self._api_key,
            's': title,
            'page': page,
            'type': 'movie'
        }
        response = self._session.get(self.URL, params=params).json()

        return self.convert_response(response)

    def convert_response(self, response: dict) -> List[object]:
        """
        Converts response dict to list of objects.

        :param response: request response dict
        :return: list of objects created from response
        """
        data_list = response.get('Search', [])
        return [self.convert_to_object(data_item) for data_item in data_list]

    def convert_to_object(self, data_item: dict) -> object:
        """
        Converts dict to object using namedtuple type.

        :param data_item: dict to convert
        :return: object constructed from dict
        """
        data_item = self.convert_dict_to_camel_case(data_item)
        return namedtuple('SearchResult', data_item.keys())(*data_item.values())

    def convert_dict_to_camel_case(self, data_item: dict) -> dict:
        """
        Converts given dict's keys to camel case.

        :param data_item: dict to convert
        :return: given dict converted to camel case
        """
        return {self.convert_to_camel_case(key): value for key, value in data_item.items()}

    @staticmethod
    def convert_to_camel_case(name: str) -> str:
        """
        Converts given string to camel case.

        :param name: string to convert
        :return: given string in camel case
        """
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
