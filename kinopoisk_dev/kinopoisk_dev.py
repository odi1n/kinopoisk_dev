from typing import List

from .field import Field
from .models import Movies, Movie, Person, PersonList
from .params.movie_params import MovieParams
from .request import get_request

LINK = "https://api.kinopoisk.dev/"
MOVIE = f'{LINK}movie'
PERSON = f'{LINK}person'
REVIEW = f'{LINK}review'
IMAGE = f'{LINK}image'
SEASON = f'{LINK}season'


class KinopoiskDev:
    def __init__(self, token: str) -> None:
        self.params = {"token": token}

    def movie(self, field: Field, search: str) -> Movie:
        response = get_request(MOVIE, params=self.params | {'field': field.value, 'search[]': search})
        return Movie(**response)

    def movies(self, params: List[MovieParams], limit: int = 100, page: int = 1) -> Movies:
        link = "&".join([param.__str__() for param in params])
        responses = get_request(f'{MOVIE}?{link}', params=self.params | {
            'limit': str(limit),
            'page': str(page)
        })
        return Movies(**responses)

    # def person(self, field: str, search: str, **kwargs):
    #     response = get_request(PERSON, params=self.params | {'field': field, 'search': search} | kwargs)
    #     if 'docs' in response:
    #         return PersonList(**response)
    #     return Person(**response)
    #
    # def review(self):
    #     pass
    #
    # def image(self):
    #     pass
    #
    # def season(self):
    #     pass
