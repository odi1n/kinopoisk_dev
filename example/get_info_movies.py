from kinopoisk_dev import KinopoiskDev, Field, MovieParams
from kinopoisk_dev.models import Movies

TOKEN = ""


def get_movies_name() -> Movies:
    """
    Поиск по названию фильма
    :return: Movies объект с информацией фильмов
    """
    kp = KinopoiskDev(token=TOKEN)
    items = kp.movies([
        MovieParams(field=Field.NAME, search='Аватар')
    ])
    return items


def get_complex_search_movie() -> Movies:
    """
    Сложная поисковая структура
    :return: Movies объект с информацией фильмов
    """
    kp = KinopoiskDev(token=TOKEN)
    items = kp.movies([
        MovieParams(field='rating.kp', search='7-10'),
        MovieParams(field=Field.YEAR, search="2017-2020"),
        MovieParams(field="typeNumber", search="2"),
        MovieParams(sortField="year", sortType=1),
        MovieParams(sortField="votes.imdb", sortType=-1),
    ], limit=1000, page=1)
    return items


if __name__ == '__main__':
    movies = get_movies_name()
    print(movies.docs[0].name)

    movies = get_complex_search_movie()
    print(movies.docs[0].name)
