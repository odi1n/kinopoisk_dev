from typing import Union, List

from field import Field
from models import MovieList, Movie, Person, PersonList
from request import get_request, get_grequest

LINK = "https://api.kinopoisk.dev/"
MOVIE = f'{LINK}movie'
PERSON = f'{LINK}person'
REVIEW = f'{LINK}review'
IMAGE = f'{LINK}image'
SEASON = f'{LINK}season'


class KinopoiskDev:
    def __init__(self, token: str) -> None:
        self.params = {"token": token}

    def movie(self, field: Field, search: str) -> Union[Movie, MovieList]:
        response = get_request(MOVIE, params=self.params | {'field': field.value, 'search': search})
        if 'docs' in response:
            raise Exception("Метод возвращает одно значение")
        return Movie(**response)

    def movie_ids(self, field: Field, ids: List[str]):
        responses = get_grequest(MOVIE, params=self.params, field=field, ids=ids)
        movies = []
        for resp in responses:
            movies.append(Movie(**resp.json()) if resp.status_code == 200 else None)
        return movies

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
