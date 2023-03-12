import asyncio

from kinopoisk_dev import KinopoiskDev, MovieAwardsField, MovieAwardsParams
from kinopoisk_dev.model import MovieAwardDocsResponseDto

TOKEN = ""


async def get_movie_awards_async() -> MovieAwardDocsResponseDto:
    """
    Асинхронный запрос.
    Получить информацию о наградах тайтлов
    :return: Список наград
    """
    kp = KinopoiskDev(token=TOKEN)
    item = await kp.amovie_awards(
        params=[
            MovieAwardsParams(keys=MovieAwardsField.PAGE, value=1),
            MovieAwardsParams(keys=MovieAwardsField.LIMIT, value=100),
        ]
    )
    return item


def get_movie_awards() -> MovieAwardDocsResponseDto:
    """
    Асинхронный запрос.
    Получить информацию о наградах тайтлов
    :return: Список наград
    """
    kp = KinopoiskDev(token=TOKEN)
    item = kp.movie_awards(
        params=[
            MovieAwardsParams(keys=MovieAwardsField.PAGE, value=1),
            MovieAwardsParams(keys=MovieAwardsField.LIMIT, value=100),
        ]
    )
    return item


if __name__ == "__main__":
    adata = asyncio.run(get_movie_awards_async())
    data = get_movie_awards()
    print(adata)
    print(data)
