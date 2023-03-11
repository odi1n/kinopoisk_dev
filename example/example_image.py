import asyncio

from kinopoisk_dev import ImageField, ImageParams, KinopoiskDev
from kinopoisk_dev.model import ImageDocsResponseDto

TOKEN = ""


async def get_image_async() -> ImageDocsResponseDto:
    """
    Асинхронный запрос.
    Получить картинки с использованием параметров
    :return: Объект с картинками
    """
    kp = KinopoiskDev(token=TOKEN)
    item = await kp.aimage(
        params=[
            ImageParams(keys=ImageField.PAGE, value=1),
            ImageParams(keys=ImageField.LIMIT, value=100),
        ]
    )
    return item


def get_image() -> ImageDocsResponseDto:
    """
    Синхронный запрос.
    Получить картинки с использованием параметров
    :return: Объект с картинками
    """
    kp = KinopoiskDev(token=TOKEN)
    item = kp.image(
        params=[
            ImageParams(keys=ImageField.PAGE, value=1),
            ImageParams(keys=ImageField.LIMIT, value=100),
        ]
    )
    return item


if __name__ == "__main__":
    adata = asyncio.run(get_image_async())
    data = get_image()
