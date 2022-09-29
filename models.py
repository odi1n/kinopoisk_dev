from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class ExternalId(BaseModel):
    _id: str
    imdb: Any


class Logo(BaseModel):
    _id: str
    url: Any


class Poster(BaseModel):
    _id: str
    url: str
    previewUrl: str


class Backdrop(BaseModel):
    _id: str
    url: str
    previewUrl: str


class Rating(BaseModel):
    _id: str
    kp: float
    imdb: float
    filmCritics: float
    russianFilmCritics: int
    await_: int = Field(..., alias='await')


class Votes(BaseModel):
    _id: str
    kp: int
    imdb: int
    filmCritics: int
    russianFilmCritics: int
    await_: int = Field(..., alias='await')


class Videos(BaseModel):
    _id: str
    trailers: List
    teasers: List


class Budget(BaseModel):
    _id: str
    value: int
    currency: str


class World(BaseModel):
    _id: str
    value: int
    currency: str


class Russia(BaseModel):
    _id: str


class Usa(BaseModel):
    _id: str
    value: int
    currency: str


class Fees(BaseModel):
    world: World
    russia: Russia
    usa: Usa
    _id: str


class Distributors(BaseModel):
    distributor: str
    distributorRelease: str


class Premiere(BaseModel):
    _id: str


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
    type: str
    spoiler: bool


class Genre(BaseModel):
    name: str


class Country(BaseModel):
    name: str


class Person(BaseModel):
    id: int
    photo: str
    name: Optional[str]
    enName: str
    enProfession: str


class Name(BaseModel):
    name: str


class Poster1(BaseModel):
    _id: str
    url: str
    previewUrl: str


class SequelsAndPrequel(BaseModel):
    _id: str
    id: int
    name: str
    enName: str
    alternativeName: str
    type: str
    poster: Poster1


class Poster2(BaseModel):
    _id: str
    url: str
    previewUrl: str


class SimilarMovy(BaseModel):
    _id: str
    id: int
    name: str
    enName: str
    alternativeName: str
    poster: Poster2


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
    items: List[Item]


class Movie(BaseModel):
    externalId: ExternalId
    logo: Logo
    poster: Poster = None
    backdrop: Backdrop = None
    rating: Rating
    votes: Votes
    videos: Videos = None
    budget: Budget = None
    fees: Fees = None
    distributors: Distributors = None
    premiere: Premiere = None
    images: Images = None
    collections: List = None
    updateDates: List[str] = None
    status: str = None
    movieLength: int = None
    productionCompanies: List[ProductionCompany] = None
    spokenLanguages: List[SpokenLanguage] = None
    id: int
    type: str
    name: str = None
    description: str = None
    slogan: str = None
    year: int = None
    facts: List[Fact] = None
    genres: List[Genre] = None
    countries: List[Country] = None
    seasonsInfo: List = None
    persons: List[Person] = None
    lists: List = None
    typeNumber: int = None
    alternativeName: str
    enName: Any
    names: List[Name]
    ageRating: Any
    ratingMpaa: str = None
    sequelsAndPrequels: List[SequelsAndPrequel] = None
    shortDescription: str = None
    similarMovies: List[SimilarMovy] = None
    technology: Technology = None
    ticketsOnSale: bool = None
    updatedAt: str = None
    imagesInfo: ImagesInfo = None
    watchability: Watchability = None
    createDate: str = None


class MovieList(BaseModel):
    docs: List[Movie]
    total: int
    limit: int
    page: int
    pages: int
