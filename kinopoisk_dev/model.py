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
    kpHD: Optional[str] = Field(description="ID из kinopoisk HD", alias="kpHD")
    imdb: Optional[str]
    tmdb: Optional[int]


class Name(BaseModel):
    name: Optional[str]


class Rating(BaseModel):
    kp: Optional[float] = Field(description="Рейтинг кинопоиска")
    imdb: Optional[float] = Field(description="Рейтинг IMDB")
    tmdb: Optional[float] = Field(description="Рейтинг TMDB")
    film_critics: Optional[float] = Field(description="Рейтинг TMDB", alias="filmCritics")
    russian_film_critics: Optional[float] = Field(description="Рейтинг TMDB", alias="russianFilmCritics")
    await_: Optional[float] = Field(description="Рейтинг TMDB", alias="await")


class Votes(BaseModel):
    kp: Optional[str] = Field(description="Количество голосов кинопоиска")
    imdb: Optional[str] = Field(description="Количество голосов IMDB")
    tmdb: Optional[int] = Field(description="Количество голосов TMDB")
    film_critics: Optional[int] = Field(description="Количество голосов кинокритиков", alias="filmCritics")
    russian_film_critics: Optional[int] = Field(description="Количество голосов кинокритиков из РФ",
                                                alias="russianFilmCritics")
    await_: Optional[int] = Field(description="Количество ожидающих выхода", alias="await")


class Logo(BaseModel):
    url: Optional[str]


class ShortImage(BaseModel):
    url: Optional[str]
    preview_url: Optional[str] = Field(alias="previewUrl")


class Video(BaseModel):
    url: Optional[str] = Field(description="Url трейлера")
    name: Optional[str]
    site: Optional[str]
    type: Optional[str]
    size: Optional[str]


class VideoTypes(BaseModel):
    trailers: Optional[List[Video]]
    teasers: List[Video]


class Person(BaseModel):
    id: Optional[int] = Field(description="Id персоны с кинопоиска")
    photo: Optional[str]
    name: Optional[str]
    en_name: Optional[str] = Field(alias="enName")
    description: Optional[str]
    profession: str
    en_profession: str = Field(alias="enProfession")


class ReviewInfo(BaseModel):
    count: Optional[int]
    positive_count: Optional[int] = Field(alias="positiveCount")
    percentage: Optional[int]


class SeasonInfo(BaseModel):
    number: Optional[str]
    episodes_count: Optional[int] = Field(alias="episodesCount")


class CurrencyValue(BaseModel):
    value: Optional[int] = Field(description="Сумма")
    currency: Optional[str] = Field(description="Валюта")


class Fees(BaseModel):
    world: Optional[CurrencyValue]
    russia: Optional[CurrencyValue]
    usa: Optional[CurrencyValue]


class Premiere(BaseModel):
    country: Optional[str]
    world: Optional[datetime] = Field(
        description="Для более релевантного поиска, используйте интервал дат 01.02.2022-01.02.2023")
    russia: Optional[datetime] = Field(
        description="Для более релевантного поиска, используйте интервал дат 01.02.2022-01.02.2023")
    digital: Optional[str]
    cinema: Optional[datetime] = Field(
        description="Для более релевантного поиска, используйте интервал дат 01.02.2022-01.02.2023")
    bluray: Optional[str]
    dvd: Optional[str]


class LinkedMovie(BaseModel):
    id: Optional[int]
    name: str
    en_name: Optional[str] = Field(alias="enName")
    alternative_name: Optional[str] = Field(alias="alternativeName")
    type: str
    poster: ShortImage


class WatchabilityItem(BaseModel):
    name: Optional[str]
    logo: Logo
    url: str


class Watchability(BaseModel):
    items: Optional[List[WatchabilityItem]]


class YearRange(BaseModel):
    start: Optional[int]
    end: Optional[int]


class Fact(BaseModel):
    value: str
    type: str
    spoiler: str


class Images(BaseModel):
    posters_count: Optional[int] = Field(alias="postersCount")
    backdrops_count: Optional[int] = Field(alias="backdropsCount")
    frames_count: int = Field(alias="framesCount")


class VendorImage(BaseModel):
    name: Optional[str]
    url: Optional[str]
    preview_url: Optional[str] = Field(alias="previewUrl")


class Movie(BaseModel):
    id: int
    external_id: ExternalId = Field(alias="externalId")
    name: Optional[str]
    alternative_name: Optional[str] = Field(alias="alternativeName")
    names: List[Name]
    type: str = Field(
        description="Тип тайтла. Доступны: movie | tv-series | cartoon | anime | animated-series | tv-show")
    type_number: int = Field(
        description="Тип тайтла в числовом обозначении. Доступны: 1 (movie) | 2 (tv-series) | 3 (cartoon) | 4 (anime) | 5 (animated-series) | 6 (tv-show)",
        alias="typeNumber")
    year: int
    description: Optional[str]
    short_description: Optional[str] = Field(alias="shortDescription")
    slogan: Optional[str]
    status: Optional[str] = Field(
        description="Статус релиза тайтла. Доступные значения: filming | pre-production | completed | announced | post-production")
    rating: Optional[Rating]
    votes: Optional[Votes]
    movie_length: Optional[int] = Field(description="Продолжительность фильма", alias="movieLength")
    rating_mpaa: Optional[str] = Field(description="Возрастной рейтинг по MPAA", alias="ratingMpaa")
    age_rating: Optional[int] = Field(description="Возрастной рейтинг", alias="ageRating")
    logo: Optional[Logo]
    poster: Optional[ShortImage]
    backdrop: Optional[ShortImage]
    videos: Optional[VideoTypes]
    genres: List[Name]
    countries: List[Name]
    persons: List[Person]
    review_info: Optional[ReviewInfo] = Field(alias="reviewInfo")
    seasons_info: Optional[SeasonInfo] = Field(alias="seasonsInfo")
    budget: Optional[CurrencyValue]
    fees: Optional[Fees]
    premiere: Optional[Premiere]
    similar_movies: Optional[List[LinkedMovie]] = Field(alias="similarMovies")
    sequels_and_prequels: Optional[List[LinkedMovie]] = Field(alias="sequelsAndPrequels")
    watchability: Optional[Watchability]
    release_years: Optional[List[YearRange]] = Field(alias="releaseYears")
    top10: Optional[int] = Field(description="Позиция тайтла в топ 10")
    top250: Optional[int] = Field(description="Позиция тайтла в топ 250")
    facts: Optional[List[Fact]]
    images_info: Optional[Images] = Field(alias="imagesInfo")
    production_companies: Optional[List[VendorImage]] = Field(alias="productionCompanies")


class PossibleValue(BaseModel):
    name: str = Field(description="Значение по которому нужно делать запрос в базу данных")
    slug: str = Field(description="Вспомогательное значение")


class PossibleValueDto(BaseModel):
    __root__: list[PossibleValue]


class MovieDocsResponseDto(Pages):
    docs: List[Movie]


class UnauthorizedErrorResponseDto(BaseModel):
    status_code: int = Field(alias="statusCode")
    message: str = Field(description="В запросе не указан токен!")
    error: str


class ForbiddenErrorResponseDto(UnauthorizedErrorResponseDto):
    pass


class ErrorResponseDto(UnauthorizedErrorResponseDto):
    pass


class Episode(BaseModel):
    movie_id: Optional[str] = Field(alias="movieId")
    season_number: Optional[str] = Field(alias="seasonNumber")
    episode_number: Optional[str] = Field(alias="episodeNumber")
    name: Optional[str]
    alternative_name: Optional[str] = Field(alias="alternativeName")
    description: Optional[str]
    date: Optional[datetime]


class Season(BaseModel):
    movie_id: Optional[str] = Field(alias="movieId")
    number: Optional[int]
    episodes_count: Optional[int] = Field(alias="episodesCount")
    episodes: Optional[List[Episode]]


class SeasonDocsResponseDto(Pages):
    docs: List[Season]


class Review(BaseModel):
    id: Optional[int]
    movie_id: Optional[int] = Field(alias="movieId")
    title: Optional[str]
    type: Optional[str]
    review: Optional[str]
    date: Optional[str]
    author: Optional[str]
    author_id: Optional[int] = Field(alias="authorId")
    user_rating: int = Field(alias="userRating")


class ReviewDocsResponseDto(Pages):
    docs: List[Review]


class PersonDocsResponseDto(BaseModel):
    docs: List[Person]


class Image(BaseModel):
    movie_id: int = Field(alias="movieId")
    type: str
    language: str
    url: str
    preview_url: str = Field(alias="previewUrl")
    height: int
    width: int


class ImageDocsResponseDto(Pages):
    docs: List[Image]
