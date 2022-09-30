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
kp = KinopoiskDev(token=TOKEN)
data = kp.movie(field=Field.KP, search="301")
```

#### Получить данные о списке фильмов по Kinopoisk ID

Возвращает информацию о списке фильмов

* `Эндпоинт` - /movie
* `Метод` - movie_ids

```python
kp = KinopoiskDev(token=TOKEN)
datas = kp.movie_ids(field=Field.KP,
                     ids=["301", "1209527", "1400126", "1445165", "4489530", "4396744", "4963617", "1435399",
                          "4400160", "4397602", '542352345', ])
```

### Параметры

#### Field

| Поля       | Значение   | Описание |
| ---------- |:----------:| :-----|
| KP    | id              | Поиск по id kinopoisk |
| IMDB  | externalId.imdb | Поиск по id imdb |
| TMDB  | externalId.tmdb | Поиск по id tmdb |