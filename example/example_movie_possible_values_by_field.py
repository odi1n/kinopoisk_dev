import asyncio
from typing import List

from kinopoisk_dev import KinopoiskDev, PossValField
from kinopoisk_dev.model import PossibleValue

TOKEN = ""


async def get_possible_values_by_field_async() -> List[PossibleValue]:
    """
    Асинхронный запрос.
    Получить все значения полей GENRES
    :return: Информация о полях GENRES
    """
    kp = KinopoiskDev(token=TOKEN)
    return await kp.apossible_values_by_field(params=PossValField.GENRES)


def get_possible_values_by_field() -> List[PossibleValue]:
    """
    Синхронный запрос.
    Получить все значения полей GENRES
    :return: Информация о полях GENRES
    """
    kp = KinopoiskDev(token=TOKEN)
    return kp.possible_values_by_field(params=PossValField.GENRES)


if __name__ == "__main__":
    adata = asyncio.run(get_possible_values_by_field_async())
    data = get_possible_values_by_field()
