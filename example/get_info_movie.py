from kinopoisk_dev import KinopoiskDev, IdField

TOKEN = ""


def get_info_kp() -> str:
    """
    Получить информацию с кинопоиска по ID,
    :return: Название фильма
    """
    kp = KinopoiskDev(token=TOKEN)
    item = kp.movie(field=IdField.KP, search="326")
    return item.name


def get_info_imdb() -> str:
    """
    Получить информацию с imdb по ID,
    :return: Название фильма
    """
    kp = KinopoiskDev(token=TOKEN)
    item = kp.movie(field=IdField.IMDB, search="326")
    return item.externalId.imdb


if __name__ == '__main__':
    print(get_info_kp())
    print(get_info_imdb())
