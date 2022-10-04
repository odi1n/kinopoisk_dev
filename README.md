<div align="center">
    <h1>Kinopoisk Dev Api</h1>
    <p>Python-модуль для взаимодействия с неофициальным <a href="https://kinopoisk.dev/">API КиноПоиска</a></p>
</div>

### Установка

```
$ pip install kinopoisk-dev
```

### Получение токена

Для получения токена необходимо перейти [kinopoisk.dev](https://kinopoisk.dev/documentation.html) и написать по
контактам.

### Movie

Методы для работы с данными о фильмах

#### Получить данные о фильме по Kinopoisk ID

Возвращает информацию о фильме.

* `Эндпоинт` - /movie
* `Метод` - movie

```python
from kinopoisk_dev import KinopoiskDev, Field

kp = KinopoiskDev(token=TOKEN)
item = kp.movie(field=Field.KP, search="301")
```

#### Сложная поисковая конструкция

Можно задавать сложные конструкции для поиска.

* `Эндпоинт` - /movie
* `Метод` - movies

##### Пример из [документации](https://kinopoisk.dev/documentation.html#%D0%BF%D0%BE%D0%B8%D1%81%D0%BA-get-5)
> Представим что нам нужно найти сериалы typeNumber - 2 с рейтингом kp от 7 до 10 которые были выпущены с 2017 по 2020 год. При этом мы ходим чтобы они были осортированы по году в порядке возрастания, но при этом были отсортированы по голосам на imdb в порядке убывания. Для этого нам придется подготовить параметры

```python
from kinopoisk_dev import KinopoiskDev, Field, MovieParams

kp = KinopoiskDev(token=TOKEN)
items = kp.movies([
    MovieParams(field='rating.kp', search='7-10'),
    MovieParams(field=Field.YEAR, search="2017-2020"),
    MovieParams(field="typeNumber", search="2"),
    MovieParams(sortField="year", sortType=1),
    MovieParams(sortField="votes.imdb", sortType=-1),
], limit=1000, page=1)
```

##### Получить информацию о списке фильмов
```python
from kinopoisk_dev import KinopoiskDev, Field, MovieParams

kp = KinopoiskDev(token=TOKEN)
items = kp.movies([
    MovieParams(field='id', search='301'),
    MovieParams(field=Field.KP, search="326"),
])
```

### Модели параметров

#### MovieParams

Имеет следующие поля

| Поля       | Тип данных| Описание                             |
| ---------- |:----------|:-------------------------------------|
| field      | str/Field | Поле по которому происходит поиск    |
| search     | str       | Данные по которым происходит поиск   |
| sortField  | str       | По какому полю происходит сортировка |
| sortType   | int       | В каком порядке выводить(1\-1)       |

### Заготовленные поля

#### Field

| Поля       | Значение   | Описание |
| ---------- |:----------:| :-----|
| KP            | id              | Поиск по id kinopoisk |
| IMDB          | externalId.imdb | Поиск по id imdb |
| TMDB          | externalId.tmdb | Поиск по id tmdb |
| TYPE          | type | Поиск по типу |
| NAME          | name | Поиск по имени |
| YEAR          | year | Поиск по году |
| TYPE_NUMBER   | typeNumber | Поиск по typeNumber |
| MOVIE_ID      | movieId | Поиск по movieId |
| LANGUAGE      | language | Поиск по языку |
| STATUS        | status | Поиск по статусу |