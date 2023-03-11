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

    def possible_values_by_field(
            self, poss_val_field: PossValField
    ) -> List[PossibleValue]:
        """
        Синхронный метод.
        Получить все возможные значения полей
        :param poss_val_field: Поле значение которого нужно нам получить
        :return: Значение полей
        """
        response = self.request.get(POSS_VAL_BY_FIELD, {"field": poss_val_field.value})
        return PossibleValueDto.parse_obj(response).__root__

    async def apossible_values_by_field(
            self, poss_val_field: PossValField
    ) -> List[PossibleValue]:
        """
        Асинхронный метод.
        Получить все возможные значения полей
        :param poss_val_field: Поле значение которого нужно нам получить
        :return: Значение полей
        """
        response = await self.arequest.get(
            POSS_VAL_BY_FIELD, {"field": poss_val_field.value}
        )
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

    def find_many_movie(self, params: List[MovieParams]) -> MovieDocsResponseDto:
        """
        Синхронный метод.
        Поиск тайтлов
        :param params: Список параметров
        :return: Список фильмов
        """
        link = "&".join([param.__str__() for param in params])
        responses = self.request.get(f"{MOVIE}?{link}")
        return MovieDocsResponseDto(**responses)

    async def afind_many_movie(self, params: List[MovieParams]) -> MovieDocsResponseDto:
        """
        Асинхронный метод.
        Поиск тайтлов
        :param params: Список параметров
        :return: Список фильмов
        """
        link = "&".join([param.__str__() for param in params])
        responses = await self.arequest.get(f"{MOVIE}?{link}")
        return MovieDocsResponseDto(**responses)

    def seasons(self, params: List[SeasonParams]) -> SeasonDocsResponseDto:
        """
        Синхронный метод.
        Поиск сезонов
        :param params: Список параметров
        :return: Список информации о сезонах
        """
        link = "&".join([param.__str__() for param in params])
        responses = self.request.get(f"{SEASON}?{link}")
        return SeasonDocsResponseDto(**responses)

    async def aseasons(self, params: List[SeasonParams]) -> SeasonDocsResponseDto:
        """
        Асинхронный метод.
        Поиск сезонов
        :param params: Список параметров
        :return: Список информации о сезонах
        """
        link = "&".join([param.__str__() for param in params])
        responses = await self.arequest.get(f"{SEASON}?{link}")
        return SeasonDocsResponseDto(**responses)

    def review(self, params: List[ReviewParams]) -> ReviewDocsResponseDto:
        """
        Синхронный метод.
        Поиск отзывов
        :param params: Список параметров
        :return: Список информации об отзывах
        """
        link = "&".join([param.__str__() for param in params])
        response = self.request.get(f"{REVIEW}?{link}")
        return ReviewDocsResponseDto(**response)

    async def areview(self, params: List[ReviewParams]) -> ReviewDocsResponseDto:
        """
        Асинхронный метод.
        Поиск отзывов
        :param params: Список параметров
        :return: Список информации об отзывах
        """
        link = "&".join([param.__str__() for param in params])
        response = await self.arequest.get(f"{REVIEW}?{link}")
        return ReviewDocsResponseDto(**response)

    def find_one_person(self, id: int) -> Person:
        """
        Синхронный метод.
        Поиск по id
        :param params: Person ID, информацию о котором нам нужно получить
        :return: Информация о Person
        """
        response = self.request.get(f"{PERSON}/{id}")
        return Person(**response)

    async def afind_one_person(self, id: int) -> Person:
        """
        Асинхронный метод.
        Поиск по id
        :param params: Person ID, информацию о котором нам нужно получить
        :return: Информация о Person
        """
        response = await self.arequest.get(f"{PERSON}/{id}")
        return Person(**response)

    def find_many_person(self, params: List[PersonParams]) -> PersonDocsResponseDto:
        """
        Синхронный метод.
        Поиск Персон
        :param params: Список параметров
        :return: Список информации о Person
        """
        link = "&".join([param.__str__() for param in params])
        response = self.request.get(f"{PERSON}?{link}")
        return PersonDocsResponseDto(**response)

    async def afind_many_person(
            self, params: List[PersonParams]
    ) -> PersonDocsResponseDto:
        """
        Асинхронный метод.
        Поиск Персон
        :param params: Список параметров
        :return: Список информации о Person
        """
        link = "&".join([param.__str__() for param in params])
        response = await self.arequest.get(f"{PERSON}?{link}")
        return PersonDocsResponseDto(**response)

    def image(self, params: List[ImageParams]) -> ImageDocsResponseDto:
        """
        Синхронный метод.
        Поиск изображений
        :param params: Список параметров
        :return: Список информации о image
        """
        link = "&".join([param.__str__() for param in params])
        response = self.request.get(f"{PERSON}?{link}")
        return ImageDocsResponseDto(**response)

    async def aimage(self, params: List[ImageParams]) -> ImageDocsResponseDto:
        """
        Асинхронный метод.
        Поиск изображений
        :param params: Список параметров
        :return: Список информации о image
        """
        link = "&".join([param.__str__() for param in params])
        response = await self.arequest.get(f"{PERSON}?{link}")
        return ImageDocsResponseDto(**response)
