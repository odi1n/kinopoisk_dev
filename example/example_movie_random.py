import asyncio

from kinopoisk_dev import KinopoiskDev
from kinopoisk_dev.model import Movie

TOKEN = ""


async def get_random_async() -> Movie:
    """
    Асинхронный запрос.
    Получить рандомный фильм
    :return: Информация о фильме
    """
    kp = KinopoiskDev(token=TOKEN)
    return await kp.arandom()


def get_random() -> Movie:
    """
    Синхронный запрос.
    Получить рандомный фильм
    :return: Информация о фильме
    """
    kp = KinopoiskDev(token=TOKEN)
    return kp.random()


if __name__ == "__main__":
    adata = asyncio.run(get_random_async())
    data = get_random()
