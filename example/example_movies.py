import asyncio
from kinopoisk_dev import MovieParams, KinopoiskDev, MovieField

kp = KinopoiskDev(token=TOKEN)


def main():
    return kp.find_many_movies(params=[
        MovieParams(value=MovieField.name, param="Аватар"),
        MovieParams(value=MovieField.page, param="1"),
        MovieParams(value=MovieField.limit, param="1000")
    ])


async def amain():
    return await kp.afind_many_movies(params=[
        MovieParams(value=MovieField.name, param="Аватар"),
        MovieParams(value=MovieField.page, param="1"),
        MovieParams(value=MovieField.limit, param="1000")
    ])


if __name__ == "__main__":
    item = main()
    print(item)

    item = asyncio.run(amain())
    print(item)
