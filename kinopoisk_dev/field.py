from enum import Enum


class IdField(Enum):
    KP = "id"
    IMDB = "externalId.imdb"


class Field(Enum):
    KP = "id"
    IMDB = "externalId.imdb"
    TMDB = "externalId.tmdb"

    TYPE = "type"
    NAME = "name"
    YEAR = "year"
    TYPE_NUMBER = "typeNumber"
    MOVIE_ID = "movieId"
    LANGUAGE = "language"
    STATUS = "status"
