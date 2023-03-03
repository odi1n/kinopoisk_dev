from kinopoisk_dev import IdField, KinopoiskDev

TOKEN = ""

kp = KinopoiskDev(token=TOKEN)


def main():
    return kp.find_one_movie(666)


async def amain():
    return await kp.afind_one_movie(666)


if __name__ == "__main__":
    item = main()
    print(item)

    item = asyncio.run(amain())
    print(item)
