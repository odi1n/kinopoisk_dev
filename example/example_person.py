import asyncio

from kinopoisk_dev import KinopoiskDev, PersonField, PersonParams
from kinopoisk_dev.model import PersonDocsResponseDto

TOKEN = ""


async def get_person_async() -> PersonDocsResponseDto:
    """
    Асинхронный запрос.
    Получить информация о персонах, с использованием параметров
    :return: Информация о персонах
    """
    kp = KinopoiskDev(token=TOKEN)
    item = await kp.afind_many_person(
        params=[
            PersonParams(keys=PersonField.PAGE, value=1),
            PersonParams(keys=PersonField.LIMIT, value=100),
        ]
    )
    return item


def get_person() -> PersonDocsResponseDto:
    """
    Синхронный запрос.
    Получить информация о персонах, с использованием параметров
    :return: Информация о персонах
    """
    kp = KinopoiskDev(token=TOKEN)
    item = kp.find_many_person(
        params=[
            PersonParams(keys=PersonField.PAGE, value=1),
            PersonParams(keys=PersonField.LIMIT, value=100),
        ]
    )
    return item


if __name__ == "__main__":
    adata = asyncio.run(get_person_async())
    data = get_person()
