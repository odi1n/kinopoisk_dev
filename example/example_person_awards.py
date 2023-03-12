import asyncio

from kinopoisk_dev import KinopoiskDev, PersonAwardsField, PersonAwardsParams
from kinopoisk_dev.model import PersonAwardDocsResponseDto

TOKEN = ""


async def get_person_awards_async() -> PersonAwardDocsResponseDto:
    """
    Асинхронный запрос.
    Получить информацию о наградах тайтлов
    :return: Список наград
    """
    kp = KinopoiskDev(token=TOKEN)
    item = await kp.aperson_awards(
        params=[
            PersonAwardsParams(keys=PersonAwardsField.PAGE, value=1),
            PersonAwardsParams(keys=PersonAwardsField.LIMIT, value=100),
        ]
    )
    return item


def get_person_awards() -> PersonAwardDocsResponseDto:
    """
    Асинхронный запрос.
    Получить информацию о наградах тайтлов
    :return: Список наград
    """
    kp = KinopoiskDev(token=TOKEN)
    item = kp.person_awards(
        params=[
            PersonAwardsParams(keys=PersonAwardsField.PAGE, value=1),
            PersonAwardsParams(keys=PersonAwardsField.LIMIT, value=100),
        ]
    )
    return item


if __name__ == "__main__":
    adata = asyncio.run(get_person_awards_async())
    data = get_person_awards()
    print(adata)
    print(data)
