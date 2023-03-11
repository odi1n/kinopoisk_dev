import asyncio

from kinopoisk_dev import KinopoiskDev
from kinopoisk_dev.model import Person

TOKEN = ""


async def get_person_async() -> Person:
    """
    Асинхронный запрос.
    Получить информация о персоне по id
    :return: Информация о персоне
    """
    kp = KinopoiskDev(token=TOKEN)
    item = await kp.afind_one_person(24262)
    return item


def get_person() -> Person:
    """
    Синхронный запрос.
    Получить информация о персоне по id
    :return: Информация о персоне
    """
    kp = KinopoiskDev(token=TOKEN)
    item = kp.find_one_person(24262)
    return item


if __name__ == "__main__":
    adata = asyncio.run(get_person_async())
    data = get_person()
