from enum import Enum


class Field(Enum):
    KP = 'id'
    IMDB = 'externalId.imdb'
    TMDB = 'externalId.tmdb'


class Fields(Enum):
    KP = 'id'
    IMDB = 'externalId.imdb'
    TMDB = 'externalId.tmdb'
    YEAR = 'year'
    NAME = 'name'
    TYPE_NUMBER = 'typeNumber'
    MOVIE_ID = 'movieId'
    TYPE = 'type'
    LANGUAGE = 'language'
