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
    __version__ = "1.0.3"

    def __init__(self, token: str) -> None:
        self.request = Request(token=token)
        self.arequest = AsyncRequest(token=token)

    def random(self) -> Movie:
        response = self.request.get(RANDOM)
        return Movie(**response)

    async def arandom(self) -> Movie:
        response = await self.arequest.get(RANDOM)
        return Movie(**response)

    def possible_values_by_field(
        self, poss_val_field: PossValField
    ) -> List[PossibleValue]:
        response = self.request.get(POSS_VAL_BY_FIELD, {"field": poss_val_field.value})
        return PossibleValueDto.parse_obj(response).__root__

    async def apossible_values_by_field(
        self, poss_val_field: PossValField
    ) -> List[PossibleValue]:
        response = await self.arequest.get(
            POSS_VAL_BY_FIELD, {"field": poss_val_field.value}
        )
        return PossibleValueDto.parse_obj(response).__root__

    def find_one_movie(self, id: int) -> Movie:
        """
        Получить информацию о фильме
        :param id: Kinopoisk id
        :return:
        """
        response = self.request.get(f"{MOVIE}/{id}")
        return Movie(**response)

    async def afind_one_movie(self, id: int) -> Movie:
        """
        Получить информацию о фильме
        :param id: Kinopoisk id
        :return:
        """
        response = await self.arequest.get(f"{MOVIE}/{id}")
        return Movie(**response)

    def find_many_movie(self, params: List[MovieParams]) -> MovieDocsResponseDto:
        """
        Сложная поисковая сортировка
        :param params: Список параметров для поиска
        :param limit: Лимит возвращаемых данных
        :param page: Номер страницы
        :return:
        """
        link = "&".join([param.__str__() for param in params])
        responses = self.request.get(f"{MOVIE}?{link}")
        return MovieDocsResponseDto(**responses)

    async def afind_many_movie(self, params: List[MovieParams]) -> MovieDocsResponseDto:
        """
        Сложная поисковая сортировка
        :param params: Список параметров для поиска
        :param limit: Лимит возвращаемых данных
        :param page: Номер страницы
        :return:
        """
        link = "&".join([param.__str__() for param in params])
        responses = await self.arequest.get(f"{MOVIE}?{link}")
        return MovieDocsResponseDto(**responses)

    def seasons(self, params: List[SeasonParams]) -> SeasonDocsResponseDto:
        link = "&".join([param.__str__() for param in params])
        responses = self.request.get(f"{SEASON}?{link}")
        return SeasonDocsResponseDto(**responses)

    async def aseasons(self, params: List[SeasonParams]) -> SeasonDocsResponseDto:
        link = "&".join([param.__str__() for param in params])
        responses = await self.arequest.get(f"{SEASON}?{link}")
        return SeasonDocsResponseDto(**responses)

    def review(self, params: List[ReviewParams]) -> ReviewDocsResponseDto:
        link = "&".join([param.__str__() for param in params])
        response = self.request.get(f"{REVIEW}?{link}")
        return ReviewDocsResponseDto(**response)

    async def areview(self, params: List[ReviewParams]) -> ReviewDocsResponseDto:
        link = "&".join([param.__str__() for param in params])
        response = await self.arequest.get(f"{REVIEW}?{link}")
        return ReviewDocsResponseDto(**response)

    def find_one_person(self, id: int) -> Person:
        response = self.request.get(f"{PERSON}/{id}")
        return Person(**response)

    async def afind_one_person(self, id: int) -> Person:
        response = await self.arequest.get(f"{PERSON}/{id}")
        return Person(**response)

    def find_many_person(self, params: List[PersonParams]) -> PersonDocsResponseDto:
        link = "&".join([param.__str__() for param in params])
        response = self.request.get(f"{PERSON}?{link}")
        return PersonDocsResponseDto(**response)

    async def afind_many_person(
        self, params: List[PersonParams]
    ) -> PersonDocsResponseDto:
        link = "&".join([param.__str__() for param in params])
        response = await self.arequest.get(f"{PERSON}?{link}")
        return PersonDocsResponseDto(**response)

    def image(self, params: List[ImageParams]) -> ImageDocsResponseDto:
        link = "&".join([param.__str__() for param in params])
        response = self.request.get(f"{PERSON}?{link}")
        return ImageDocsResponseDto(**response)

    async def aimage(self, params: List[ImageParams]) -> ImageDocsResponseDto:
        link = "&".join([param.__str__() for param in params])
        response = await self.arequest.get(f"{PERSON}?{link}")
        return ImageDocsResponseDto(**response)
