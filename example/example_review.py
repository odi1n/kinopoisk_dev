import asyncio

from kinopoisk_dev import KinopoiskDev, ReviewField, ReviewParams
from kinopoisk_dev.model import ReviewDocsResponseDto

TOKEN = ""


async def get_review_async() -> ReviewDocsResponseDto:
    """
    Асинхронный запрос.
    Поиск отзывов, с использованием параметров
    :return: Отзывы
    """
    kp = KinopoiskDev(token=TOKEN)
    item = await kp.areview(
        params=[
            ReviewParams(keys=ReviewField.PAGE, value=1),
            ReviewParams(keys=ReviewField.LIMIT, value=100),
        ]
    )
    return item


def get_review() -> ReviewDocsResponseDto:
    """
    Синхронный запрос.
    Поиск отзывов, с использованием параметров
    :return: Отзывы
    """
    kp = KinopoiskDev(token=TOKEN)
    item = kp.review(
        params=[
            ReviewParams(keys=ReviewField.PAGE, value=1),
            ReviewParams(keys=ReviewField.LIMIT, value=100),
        ]
    )
    return item


if __name__ == "__main__":
    adata = asyncio.run(get_review_async())
    data = get_review()
