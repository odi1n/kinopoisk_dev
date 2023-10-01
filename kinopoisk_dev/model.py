from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Pages(BaseModel):
    total: int = Field(description="Общее количество результатов")
    limit: int = Field(description="Количество результатов на странице")
    page: int = Field(description="Текущая страница")
    pages: int = Field(description="Сколько страниц всего")


class ExternalId(BaseModel):
    kpHD: Optional[str] = Field(
        description="ID из kinopoisk HD",
        example="48e8d0acb0f62d8585101798eaeceec5",
    )
    imdb: Optional[str] = Field(example="tt0232500")
    tmdb: Optional[int] = Field(example=9799)


class Name(BaseModel):
    name: Optional[str]


class Rating(BaseModel):
    kp: Optional[float] = Field(description="Рейтинг кинопоиска", example=6.2)
    imdb: Optional[float] = Field(description="Рейтинг IMDB", example=8.4)
    tmdb: Optional[float] = Field(description="Рейтинг TMDB", example=3.2)
    filmCritics: Optional[float] = Field(description="Рейтинг кинокритиков", example=10)
    russianFilmCritics: Optional[float] = Field(
        description="Рейтинг кинокритиков из РФ", example=5.1
    )
    await_: Optional[float] = Field(
        alias="await",
        description="Рейтинг основанный на ожиданиях пользователей",
        example=6.1,
    )


class Votes(BaseModel):
    kp: Optional[str] = Field(example=60000)
    imdb: Optional[str] = Field(example=50000)
    tmdb: Optional[float] = Field(example=10000)
    filmCritics: Optional[float] = Field(
        description="Количество голосов кинокритиков", example=10000
    )
    russianFilmCritics: Optional[float] = Field(
        description="Количество голосов кинокритиков из РФ", example=4000
    )
    await_: Optional[float] = Field(
        alias="await", description="Количество ожидающих выхода", example=34000
    )


class Logo(BaseModel):
    url: Optional[str] = Field(
        description="Чтобы найти фильмы с этим полем, используйте: `!null`"
    )


class ShortImage(BaseModel):
    url: Optional[str] = Field(
        description="Чтобы найти фильмы с этим полем, используйте: `!null`"
    )
    previewUrl: Optional[str] = Field(
        description="Чтобы найти фильмы с этим полем, используйте: `!null`"
    )


class Video(BaseModel):
    url: Optional[str] = Field(
        description="Url трейлера",
        example="https://www.youtube.com/embed/ZsJz2TJAPjw",
    )
    name: Optional[str] = Field(example="Official Trailer")
    site: Optional[str] = Field(example="youtube")
    type: Optional[str] = Field(example="TRAILER")
    size: Optional[float]


class VideoTypes(BaseModel):
    trailers: Optional[List[Video]]
    teasers: List[Video]


class PersonInMovie(BaseModel):
    id: Optional[float] = Field(description="Id персоны с кинопоиска", example=6317)
    photo: Optional[str] = Field(
        example="https://st.kp.yandex.net/images/actor_iphone/iphone360_6317.jpg"
    )
    name: Optional[str] = Field(example="Пол Уокер")
    enName: Optional[str] = Field(example="Paul Walker")
    description: Optional[str]
    profession: str
    enProfession: str


class ReviewInfo(BaseModel):
    count: Optional[int]
    positiveCount: Optional[int]
    percentage: Optional[int]


class SeasonInfo(BaseModel):
    number: Optional[str]
    episodesCount: Optional[int]


class CurrencyValue(BaseModel):
    value: Optional[int] = Field(description="Сумма", example=207283)
    currency: Optional[str] = Field(description="Валюта", example="€")


class Fees(BaseModel):
    world: Optional[CurrencyValue]
    russia: Optional[CurrencyValue]
    usa: Optional[CurrencyValue]


class Premiere(BaseModel):
    country: Optional[str] = Field(example="США")
    world: Optional[datetime] = Field(
        description="Для более релевантного поиска, используйте интервал дат 01.02.2022-01.02.2023",
        example="2023-02-25T02:44:39.359Z",
    )
    russia: Optional[datetime] = Field(
        description="Для более релевантного поиска, используйте интервал дат 01.02.2022-01.02.2023",
        example="2023-02-25T02:44:39.359Z",
    )
    digital: Optional[str]
    cinema: Optional[datetime] = Field(
        description="Для более релевантного поиска, используйте интервал дат 01.02.2022-01.02.2023",
        example="2023-02-25T02:44:39.359Z",
    )
    bluray: Optional[str]
    dvd: Optional[str]


class LinkedMovie(BaseModel):
    id: Optional[int]
    name: Optional[str]
    enName: Optional[str]
    alternativeName: Optional[str]
    type: Optional[str]
    poster: ShortImage


class WatchabilityItem(BaseModel):
    name: Optional[str]
    logo: Logo
    url: str


class Watchability(BaseModel):
    items: Optional[List[WatchabilityItem]]


class YearRange(BaseModel):
    start: Optional[int] = Field(description="Год начала", example=2022)
    end: Optional[int] = Field(description="Год окончания", example=2023)


class Fact(BaseModel):
    value: str
    type: str
    spoiler: bool


class Images(BaseModel):
    postersCount: Optional[int]
    backdropsCount: Optional[int]
    framesCount: int


class VendorImage(BaseModel):
    name: Optional[str]
    url: Optional[str]
    previewUrl: Optional[str]


class Movie(BaseModel):
    id: Optional[int] = Field(..., description="Id фильма с кинопоиска", example=666)
    externalId: Optional[ExternalId]
    name: Optional[str] = Field(example="Человек паук")
    alternativeName: Optional[str] = Field(example="Spider man")
    names: Optional[List[Name]]
    type: Optional[str] = Field(
        description="Тип тайтла. Доступны: movie | tv-series | cartoon | anime | animated-series | tv-show",
        example="movie",
    )
    typeNumber: Optional[int] = Field(
        description="Тип тайтла в числовом обозначении. Доступны: 1 (movie) | 2 (tv-series) | 3 (cartoon) | 4 (anime) | 5 (animated-series) | 6 (tv-show)",
        example=1,
    )
    year: Optional[int] = Field(
        description="Год премьеры. При поиске по этому полю, можно использовать интервалы 1860-2030",
        example=2023,
    )
    description: Optional[str] = Field(description="Описание тайтла")
    shortDescription: Optional[str] = Field(description="Сокращенное описание")
    slogan: Optional[str] = Field(description="Слоган")
    status: Optional[str] = Field(
        description="Статус релиза тайтла. Доступные значения: filming | pre-production | completed | announced | post-production",
        example="completed",
    )
    rating: Optional[Rating]
    votes: Optional[Votes]
    movieLength: Optional[int] = Field(
        description="Продолжительность фильма", example=120
    )
    ratingMpaa: Optional[str] = Field(
        description="Возрастной рейтинг по MPAA", example="pg13"
    )
    ageRating: Optional[int] = Field(description="Возрастной рейтинг", example="16")
    logo: Optional[Logo]
    poster: Optional[ShortImage]
    backdrop: Optional[ShortImage]
    videos: Optional[VideoTypes]
    genres: Optional[List[Name]]
    countries: Optional[List[Name]]
    persons: Optional[List[PersonInMovie]]
    reviewInfo: Optional[ReviewInfo]
    seasonsInfo: Optional[SeasonInfo]
    budget: Optional[CurrencyValue]
    fees: Optional[Fees]
    premiere: Optional[Premiere]
    similarMovies: Optional[List[LinkedMovie]]
    sequelsAndPrequels: Optional[List[LinkedMovie]]
    watchability: Optional[Watchability]
    releaseYears: Optional[List[YearRange]]
    top10: Optional[int] = Field(
        ddescription="Позиция тайтла в топ 10. Чтобы найти фильмы участвующие в рейтинге используйте: `!null`",
        example=1,
    )
    top250: Optional[int] = Field(
        description="Позиция тайтла в топ 250. Чтобы найти фильмы участвующие в рейтинге используйте: `!null`",
        example=200,
    )
    enName: Optional[str]
    facts: Optional[List[Fact]]
    imagesInfo: Optional[Images]
    productionCompanies: Optional[List[VendorImage]]


class PossibleValue(BaseModel):
    name: str = Field(
        description="Значение по которому нужно делать запрос в базу данных"
    )
    slug: str = Field(description="Вспомогательное значение")


class PossibleValueDto(BaseModel):
    __root__: List[PossibleValue]


class MovieDocsResponseDto(Pages):
    docs: List[Movie]


class UnauthorizedErrorResponseDto(BaseModel):
    statusCode: int
    message: str = Field(description="В запросе не указан токен!")
    error: str


class ForbiddenErrorResponseDto(UnauthorizedErrorResponseDto):
    pass


class ErrorResponseDto(UnauthorizedErrorResponseDto):
    pass


class Episode(BaseModel):
    movieId: Optional[int]
    seasonNumber: Optional[int]
    episodeNumber: Optional[int]
    name: Optional[str]
    alternativeName: Optional[str]
    description: Optional[str]
    date: Optional[str]


class Season(BaseModel):
    movieId: Optional[str]
    number: Optional[int]
    episodesCount: Optional[int]
    episodes: Optional[List[Episode]]


class SeasonDocsResponseDto(Pages):
    docs: List[Season]


class Review(BaseModel):
    id: Optional[int]
    movieId: Optional[int]
    title: Optional[str]
    type: Optional[str]
    review: Optional[str]
    date: Optional[str]
    author: Optional[str]
    authorId: Optional[int]
    userRating: Optional[int]


class ReviewDocsResponseDto(Pages):
    docs: List[Review]


class BirthPlace(BaseModel):
    value: Optional[str]


class DeathPlace(BaseModel):
    value: Optional[str]


class Spouses(BaseModel):
    id: Optional[int]
    name: Optional[str]
    divorced: Optional[bool]
    divorcedReason: Optional[str]
    sex: Optional[str]
    children: Optional[int]
    relation: Optional[str]


class Profession(BaseModel):
    value: Optional[str]


class FactInPerson(BaseModel):
    value: Optional[str]


class MovieInPerson(BaseModel):
    id: int
    name: Optional[str]
    alternativeName: Optional[str]
    rating: Optional[int]
    general: Optional[bool]
    description: Optional[str]
    enProfession: Optional[str]


class Person(BaseModel):
    id: int
    name: Optional[str]
    enName: Optional[str]
    photo: Optional[str]
    sex: Optional[str]
    growth: Optional[int]
    birthday: Optional[str]
    death: Optional[str]
    age: Optional[int]
    birthPlace: Optional[List[BirthPlace]]
    deathPlace: Optional[List[DeathPlace]]
    spouses: Optional[List[Spouses]]
    countAwards: Optional[int]
    profession: Optional[List[Profession]]
    facts: Optional[List[FactInPerson]]
    movies: Optional[List[MovieInPerson]]


class PersonDocsResponseDto(BaseModel):
    docs: List[Person]


class Image(BaseModel):
    id: int
    type: Optional[str]
    language: Optional[str]
    url: Optional[str]
    previewUrl: Optional[str]
    height: Optional[int]
    width: Optional[int]


class ImageDocsResponseDto(Pages):
    docs: List[Image]