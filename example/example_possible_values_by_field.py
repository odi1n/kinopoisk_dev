import asyncio

from kinopoisk_dev import KinopoiskDev, PossValField

TOKEN = ""

kp = KinopoiskDev(token=TOKEN)


def main():
    return kp.possible_values_by_field(poss_val_field=PossValField.GENRES)


async def amain():
    return await kp.apossible_values_by_field(poss_val_field=PossValField.GENRES)


if __name__ == '__main__':
    item = main()
    print(item)

    item = asyncio.run(amain())
    print(item)
