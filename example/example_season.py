import asyncio

from kinopoisk_dev import KinopoiskDev, SeasonField, SeasonParams
from kinopoisk_dev.model import SeasonDocsResponseDto

TOKEN = ""


async def get_season_async() -> SeasonDocsResponseDto:
    """
    Асинхронный запрос.
    Получить информацию о сезонах с использованием параметров
    :return: Список сезонов
    """
    kp = KinopoiskDev(token=TOKEN)
    item = await kp.aseasons(
        params=[
            SeasonParams(keys=SeasonField.PAGE, value=1),
            SeasonParams(keys=SeasonField.LIMIT, value=100),
        ]
    )
    return item


def get_seasons() -> SeasonDocsResponseDto:
    """
    Синхронный запрос.
    Получить информацию о сезонах с использованием параметров
    :return: Список сезонов
    """
    kp = KinopoiskDev(token=TOKEN)
    item = kp.seasons(
        params=[
            SeasonParams(keys=SeasonField.PAGE, value=1),
            SeasonParams(keys=SeasonField.LIMIT, value=100),
        ]
    )
    return item


if __name__ == "__main__":
    adata = asyncio.run(get_season_async())
    data = get_seasons()
