from typing import List

from .fields import PossValField
from .model import (
    ImageDocsResponseDto,
    Movie,
    MovieDocsResponseDto,
    Person,
    PersonDocsResponseDto,
    PossibleValue,
    PossibleValueDto,
    ReviewDocsResponseDto,
    SeasonDocsResponseDto,
)
from .params import ImageParams, MovieParams, PersonParams, ReviewParams, SeasonParams
from .request import AsyncRequest, Request
from .untils import get_params
from .urls import MOVIE, PERSON, POSS_VAL_BY_FIELD, RANDOM, REVIEW, SEASON


class KinopoiskDev:
    """
    Реализация обертки на сервис kinopoisk.dev
    """

    __version__ = "1.0.3"

    def __init__(self, token: str) -> None:
        self.request = Request(token=token)
        self.arequest = AsyncRequest(token=token)

    def random(self) -> Movie:
        """
        Синхронный метод.
        Получить рандомный тайтл из базы
        :return: Фильм
        """
        response = self.request.get(RANDOM)
        return Movie(**response)

    async def arandom(self) -> Movie:
        """
        Асинхронный метод.
        Получить рандомный тайтл из базы
        :return: Фильм
        """
        response = await self.arequest.get(RANDOM)
        return Movie(**response)

    def possible_values_by_field(self, params: PossValField) -> List[PossibleValue]:
        """
        Синхронный метод.
        Получить все возможные значения полей
        :param params: Поле значение которого нужно нам получить
        :return: Значение полей
        """
        response = self.request.get(POSS_VAL_BY_FIELD, {"field": params.value})
        return PossibleValueDto.parse_obj(response).__root__

    async def apossible_values_by_field(
        self, params: PossValField
    ) -> List[PossibleValue]:
        """
        Асинхронный метод.
        Получить все возможные значения полей
        :param params: Поле значение которого нужно нам получить
        :return: Значение полей
        """
        response = await self.arequest.get(POSS_VAL_BY_FIELD, {"field": params.value})
        return PossibleValueDto.parse_obj(response).__root__

    def find_one_movie(self, id: int) -> Movie:
        """
        Синхронный метод.
        Поиск по id
        :param id: Kinopoisk id, параметр по которому получим информацию о фильме
        :return: Фильм
        """
        response = self.request.get(f"{MOVIE}/{id}")
        return Movie(**response)

    async def afind_one_movie(self, id: int) -> Movie:
        """
        Асинхронный метод.
        Поиск по id
        :param id: Kinopoisk id, параметр по которому получим информацию о фильме
        :return: Фильм
        """
        response = await self.arequest.get(f"{MOVIE}/{id}")
        return Movie(**response)

    def find_many_movie(self, params: List[MovieParams] = None) -> MovieDocsResponseDto:
        """
        Синхронный метод.
        Поиск тайтлов
        :param params: Список параметров
        :return: Список фильмов
        """
        responses = self.request.get(f"{MOVIE}?{get_params(params)}")
        return MovieDocsResponseDto(**responses)

    async def afind_many_movie(
        self, params: List[MovieParams] = None
    ) -> MovieDocsResponseDto:
        """
        Асинхронный метод.
        Поиск тайтлов
        :param params: Список параметров
        :return: Список фильмов
        """
        responses = await self.arequest.get(f"{MOVIE}?{get_params(params)}")
        return MovieDocsResponseDto(**responses)

    def seasons(self, params: List[SeasonParams] = None) -> SeasonDocsResponseDto:
        """
        Синхронный метод.
        Поиск сезонов
        :param params: Список параметров
        :return: Список информации о сезонах
        """
        responses = self.request.get(f"{SEASON}?{get_params(params)}")
        return SeasonDocsResponseDto(**responses)

    async def aseasons(
        self, params: List[SeasonParams] = None
    ) -> SeasonDocsResponseDto:
        """
        Асинхронный метод.
        Поиск сезонов
        :param params: Список параметров
        :return: Список информации о сезонах
        """
        responses = await self.arequest.get(f"{SEASON}?{get_params(params)}")
        return SeasonDocsResponseDto(**responses)

    def review(self, params: List[ReviewParams] = None) -> ReviewDocsResponseDto:
        """
        Синхронный метод.
        Поиск отзывов
        :param params: Список параметров
        :return: Список информации об отзывах
        """
        response = self.request.get(f"{REVIEW}?{get_params(params)}")
        return ReviewDocsResponseDto(**response)

    async def areview(self, params: List[ReviewParams] = None) -> ReviewDocsResponseDto:
        """
        Асинхронный метод.
        Поиск отзывов
        :param params: Список параметров
        :return: Список информации об отзывах
        """
        response = await self.arequest.get(f"{REVIEW}?{get_params(params)}")
        return ReviewDocsResponseDto(**response)

    def find_one_person(self, id: int) -> Person:
        """
        Синхронный метод.
        Поиск по id
        :param id: Person ID, информацию о котором нам нужно получить
        :return: Информация о Person
        """
        response = self.request.get(f"{PERSON}/{id}")
        return Person(**response)

    async def afind_one_person(self, id: int) -> Person:
        """
        Асинхронный метод.
        Поиск по id
        :param id: Person ID, информацию о котором нам нужно получить
        :return: Информация о Person
        """
        response = await self.arequest.get(f"{PERSON}/{id}")
        return Person(**response)

    def find_many_person(
        self, params: List[PersonParams] = None
    ) -> PersonDocsResponseDto:
        """
        Синхронный метод.
        Поиск Персон
        :param params: Список параметров
        :return: Список информации о Person
        """
        response = self.request.get(f"{PERSON}?{get_params(params)}")
        return PersonDocsResponseDto(**response)

    async def afind_many_person(
        self, params: List[PersonParams] = None
    ) -> PersonDocsResponseDto:
        """
        Асинхронный метод.
        Поиск Персон
        :param params: Список параметров
        :return: Список информации о Person
        """
        response = await self.arequest.get(f"{PERSON}?{get_params(params)}")
        return PersonDocsResponseDto(**response)

    def image(self, params: List[ImageParams] = None) -> ImageDocsResponseDto:
        """
        Синхронный метод.
        Поиск изображений
        :param params: Список параметров
        :return: Список информации о image
        """
        response = self.request.get(f"{PERSON}?{get_params(params)}")
        return ImageDocsResponseDto(**response)

    async def aimage(self, params: List[ImageParams] = None) -> ImageDocsResponseDto:
        """
        Асинхронный метод.
        Поиск изображений
        :param params: Список параметров
        :return: Список информации о image
        """
        response = await self.arequest.get(f"{PERSON}?{get_params(params)}")
        return ImageDocsResponseDto(**response)
