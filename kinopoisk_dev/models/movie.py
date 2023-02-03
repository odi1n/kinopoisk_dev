from __future__ import annotations

from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel, Field

from .page import Page


class Base1(BaseModel):
    _id: str
    imdb: Any


class ExternalId(Base1):
    pass


class Logo(Base1):
    pass


class Base2(BaseModel):
    _id: str
    url: Optional[str]
    previewUrl: Optional[str]


class Poster(Base2):
    pass


class Backdrop(Base2):
    pass


class Base3(BaseModel):
    _id: str
    kp: Optional[float]
    imdb: Optional[float]
    filmCritics: Optional[float]
    russianFilmCritics: Optional[int]
    await_: int = Field(default=None, alias='await')


class Rating(Base3):
    pass


class Votes(Base3):
    pass


class Trailer(BaseModel):
    _id: str
    url: str
    name: str
    site: str
    size: Optional[int]
    type: Optional[str]


class Videos(BaseModel):
    _id: str
    trailers: List[Trailer]
    teasers: List


class Base4(BaseModel):
    _id: str
    value: int = 0
    currency: Optional[str]


class Budget(Base4):
    pass


class World(Base4):
    pass


class Russia(Base4):
    pass


class Usa(Base4):
    pass


class Fees(BaseModel):
    world: Optional[World]
    russia: Optional[Russia]
    usa: Optional[Usa]
    _id: str


class Distributors(BaseModel):
    distributor: Optional[str]
    distributorRelease: Optional[str]


class Premiere(BaseModel):
    _id: str
    country: Optional[str]
    world: Optional[datetime]


class Images(BaseModel):
    _id: str
    framesCount: int


class ProductionCompany(BaseModel):
    name: str
    url: Optional[str]
    previewUrl: Optional[str]


class SpokenLanguage(BaseModel):
    name: str
    nameEn: str


class Fact(BaseModel):
    value: str
    type: Optional[str]
    spoiler: Optional[bool]


class Genre(BaseModel):
    name: str


class Country(BaseModel):
    name: str


class Person(BaseModel):
    id: int
    photo: str
    name: Optional[str]
    enName: Optional[str]
    enProfession: str
    description: Optional[str]


class Name(BaseModel):
    name: str


class SequelsAndPrequel(BaseModel):
    _id: str
    id: Optional[int]
    name: Optional[str]
    enName: Optional[str]
    alternativeName: Optional[str]
    type: Optional[str]
    poster: Optional[Poster]


class SimilarMovy(BaseModel):
    _id: str
    id: int
    name: Optional[str]
    enName: Optional[str]
    alternativeName: Optional[str]
    poster: Poster


class Technology(BaseModel):
    _id: str
    hasImax: bool
    has3D: bool


class ImagesInfo(BaseModel):
    _id: str
    framesCount: int


class Logo1(BaseModel):
    _id: str
    url: str


class Item(BaseModel):
    _id: str
    name: str
    logo: Logo1
    url: str


class Watchability(BaseModel):
    _id: str
    items: Optional[List[Item]]


class Movie(BaseModel):
    externalId: Optional[ExternalId]
    logo: Optional[Logo]
    poster: Optional[Poster]
    backdrop: Optional[Backdrop]
    rating: Rating
    votes: Votes
    videos: Optional[Videos]
    budget: Optional[Budget]
    fees: Optional[Fees]
    distributors: Optional[Distributors]
    premiere: Optional[Premiere]
    images: Optional[Images]
    collections: Optional[List]
    updateDates: Optional[List[str]]
    status: Optional[str]
    movieLength: Optional[int]
    productionCompanies: Optional[List[ProductionCompany]]
    spokenLanguages: Optional[List[SpokenLanguage]]
    id: int
    type: Optional[str]
    name: Optional[str]
    description: Optional[str]
    slogan: Optional[str]
    year: Optional[int]
    facts: Optional[List[Fact]]
    genres: Optional[List[Genre]]
    countries: Optional[List[Country]]
    seasonsInfo: List = None
    persons: Optional[List[Person]]
    lists: List = None
    typeNumber: Optional[int]
    alternativeName: Optional[str]
    enName: Any
    names: Optional[List[Name]]
    ageRating: Any
    ratingMpaa: Optional[str]
    sequelsAndPrequels: Optional[List[SequelsAndPrequel]]
    shortDescription: Optional[str]
    similarMovies: Optional[List[SimilarMovy]]
    technology: Optional[Technology]
    ticketsOnSale: Optional[bool]
    updatedAt: Optional[str]
    imagesInfo: Optional[ImagesInfo]
    watchability: Optional[Watchability]
    createDate: Optional[str]


class Movies(Page):
    docs: List[Movie]
