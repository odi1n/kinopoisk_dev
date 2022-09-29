from typing import Union

from models import Movie, MovieList
from request import get_request

LINK = "https://api.kinopoisk.dev/"
MOVIE = f'{LINK}movie'
PERSON = f'{LINK}person'
REVIEW = f'{LINK}review'
IMAGE = f'{LINK}image'
SEASON = f'{LINK}season'


class KinopoiskDev:
    def __init__(self, token: str) -> None:
        self.params = {"token": token}

    def movie(self, field: str, search: str, **kwargs) -> Union[Movie, MovieList]:
        response = get_request(MOVIE, params=self.params | {'field': field, 'search': search} | kwargs)
        if 'docs' in response:
            return MovieList(**response)
        return Movie(**response)
