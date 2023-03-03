import asyncio

from kinopoisk_dev import KinopoiskDev

TOKEN = ""

kp = KinopoiskDev(token=TOKEN)


def main():
    return kp.random()


async def amain():
    return await kp.arandom()


if __name__ == '__main__':
    item = main()
    print(item)

    item = asyncio.run(amain())
    print(item)
