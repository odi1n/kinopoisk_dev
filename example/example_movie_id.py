import asyncio

from kinopoisk_dev import KinopoiskDev
from kinopoisk_dev.model import Movie

TOKEN = ""


async def get_movie_async() -> Movie:
    """
    Асинхронный запрос.
    Получить информацию о фильмы по kp id
    :return: Информация о фильме
    """
    kp = KinopoiskDev(token=TOKEN)
    return await kp.afind_one_movie(666)


def get_movie() -> Movie:
    """
    Синхронный запрос.
    Получить информацию о фильмы по kp id
    :return: Информация о фильме
    """
    kp = KinopoiskDev(token=TOKEN)
    return kp.find_one_movie(666)


if __name__ == "__main__":
    adata = asyncio.run(get_movie_async())
    data = get_movie()
