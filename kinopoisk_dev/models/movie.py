from __future__ import annotations

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
    url: str = None
    previewUrl: str = None


class Poster(Base2):
    pass


class Backdrop(Base2):
    pass


class Base3(BaseModel):
    _id: str
    kp: float = None
    imdb: float = None
    filmCritics: float = None
    russianFilmCritics: int = None
    await_: int = Field(default=None, alias='await')


class Rating(Base3):
    pass


class Votes(Base3):
    pass


class Videos(BaseModel):
    _id: str
    trailers: List
    teasers: List


class Base4(BaseModel):
    _id: str
    value: int = 0
    currency: str = None


class Budget(Base4):
    pass


class World(Base4):
    pass


class Russia(BaseModel):
    _id: str


class Usa(Base4):
    pass


class Fees(BaseModel):
    world: World
    russia: Russia
    usa: Usa
    _id: str


class Distributors(BaseModel):
    distributor: str = None
    distributorRelease: str = None


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
    enName: str = None
    enProfession: str


class Name(BaseModel):
    name: str


class SequelsAndPrequel(BaseModel):
    _id: str
    id: int = None
    name: str = None
    enName: str = None
    alternativeName: str = None
    type: str = None
    poster: Poster = None


class SimilarMovy(BaseModel):
    _id: str
    id: int
    name: str
    enName: str
    alternativeName: str
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
    items: List[Item] = None


class Movie(BaseModel):
    externalId: ExternalId
    logo: Logo = None
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
    alternativeName: str = None
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


class MovieList(Page):
    docs: List[Movie]