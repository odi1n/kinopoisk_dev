import asyncio

from kinopoisk_dev import KinopoiskDev, MovieField, MovieParams
from kinopoisk_dev.model import MovieDocsResponseDto

TOKEN = ""


async def get_movies_async() -> MovieDocsResponseDto:
    """
    Асинхронный запрос.
    Получить информацию о фильмы с использованием параметров
    :return: Список фильмов
    """
    kp = KinopoiskDev(token=TOKEN)
    item = await kp.afind_many_movie(
        params=[
            MovieParams(keys=MovieField.PAGE, value=1),
            MovieParams(keys=MovieField.LIMIT, value=100),
        ]
    )
    return item


def get_movies() -> MovieDocsResponseDto:
    """
    Асинхронный запрос.
    Получить информацию о фильмы с использованием параметров
    :return: Список фильмов
    """
    kp = KinopoiskDev(token=TOKEN)
    item = kp.find_many_movie(
        params=[
            MovieParams(keys=MovieField.PAGE, value=1),
            MovieParams(keys=MovieField.LIMIT, value=100),
        ]
    )
    return item


if __name__ == "__movie__":
    adata = asyncio.run(get_movies_async())
    data = get_movies()
