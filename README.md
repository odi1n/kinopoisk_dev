<div align="center">
    <h1>Kinopoisk Dev Api</h1>
    <p>Python-модуль для взаимодействия с неофициальным <a href="https://kinopoisk.dev/">API КиноПоиска</a></p>
</div>

## Установка

### Pip

```
pip install kinopoisk-dev
```

### Poetry

```
poetry add kinopoisk-dev
```

## Получение токена

Для получения токена необходимо перейти [kinopoisk.dev](https://kinopoisk.dev/documentation.html) и написать по
контактам.

## Методы взаимодействия

### Random

Получить рандомный тайтл из базы

- Endpoint - `/v1/movie/random`
- [Примеры](./example/example_movie_random.py)

#### Async

```python
import asyncio
from kinopoisk_dev import KinopoiskDev

kp = KinopoiskDev(token=TOKEN)
item = asyncio.run(kp.arandom())
```

#### Sync

```python
from kinopoisk_dev import KinopoiskDev

kp = KinopoiskDev(token=TOKEN)
item = kp.random()
```

### Possible values by field

Получить все возможные значения полей

- Endpoint - `/v1/movie/possible-values-by-field`
- [Примеры](./example/example_movie_possible_values_by_field.py)

#### Async

```python
import asyncio
from kinopoisk_dev import KinopoiskDev, PossValField

kp = KinopoiskDev(token=TOKEN)
item = asyncio.run(kp.apossible_values_by_field(params=PossValField.GENRES))
```

#### Sync

```python
from kinopoisk_dev import KinopoiskDev, PossValField

kp = KinopoiskDev(token=TOKEN)
item = kp.possible_values_by_field(params=PossValField.GENRES)
```

### Moview Awards

Награды тайтлов

- Ендпоинт - `/v1.1/movie/awards`
- [Примеры](./example/example_movie_awards.py)

#### Async

```python
import asyncio
from kinopoisk_dev import KinopoiskDev, MovieAwardsField, MovieAwardsParams

kp = KinopoiskDev(token=TOKEN)
item = asyncio.run(await kp.amovie_awards(params=[
    MovieAwardsParams(keys=MovieAwardsField.PAGE, value=1),
    MovieAwardsParams(keys=MovieAwardsField.LIMIT, value=100),
]))
```

#### Sync

```python
from kinopoisk_dev import KinopoiskDev, MovieAwardsField, MovieAwardsParams

kp = KinopoiskDev(token=TOKEN)
item = kp.movie_awards(params=[
    MovieAwardsParams(keys=MovieAwardsField.PAGE, value=1),
    MovieAwardsParams(keys=MovieAwardsField.LIMIT, value=100),
])
```

### Movies

Поиск тайтлов

- Ендпоинт - `/v1/movie/`
- [Примеры](./example/example_movie.py)

#### Async

```python
import asyncio
from kinopoisk_dev import KinopoiskDev, MovieParams, MovieField

kp = KinopoiskDev(token=TOKEN)
items = asyncio.run(kp.afind_many_movies(params=[
    MovieParams(keys=MovieField.name, value="Аватар"),
    MovieParams(keys=MovieField.page, value="1"),
    MovieParams(keys=MovieField.limit, value="1000")
]))
```

#### Sync

```python
from kinopoisk_dev import KinopoiskDev, MovieParams, MovieField

kp = KinopoiskDev(token=TOKEN)
items = kp.find_many_movies(params=[
    MovieParams(keys=MovieField.name, value="Аватар"),
    MovieParams(keys=MovieField.page, value="1"),
    MovieParams(keys=MovieField.limit, value="1000")
])
```

### Movie

Поиск по id

- Ендпоинт - `/v1/movie/{id}`
- [Примеры](./example/example_movie_id.py)

#### Async

```python
from kinopoisk_dev import KinopoiskDev

kp = KinopoiskDev(token=TOKEN)
item = asyncio.run(kp.afind_one_movie(666))
```

#### Sync

```python
from kinopoisk_dev import KinopoiskDev

kp = KinopoiskDev(token=TOKEN)
item = kp.find_one_movie(666)
```

### Season

- Ендпоинт - `/v1/season`
- [Пример](./example/example_season.py)

#### Async

```python
import asyncio
from kinopoisk_dev import KinopoiskDev, SeasonParams, SeasonField

kp = KinopoiskDev(token=TOKEN)
item = asyncio.run(kp.aseasons(params=[
    SeasonParams(keys=SeasonField.PAGE, value=1),
    SeasonParams(keys=SeasonField.LIMIT, value=100)
]))
```

#### Sync

```python
from kinopoisk_dev import KinopoiskDev, SeasonParams, SeasonField

kp = KinopoiskDev(token=TOKEN)
item = kp.seasons(params=[
    SeasonParams(keys=SeasonField.PAGE, value=1),
    SeasonParams(keys=SeasonField.LIMIT, value=100)
])
```

### Review

- Ендпоинт - `/v1/review`
- [Пример](./example/example_review.py)

#### Async

```python
import asyncio

from kinopoisk_dev import KinopoiskDev, ReviewParams, ReviewField

kp = KinopoiskDev(token=TOKEN)
item = asyncio.run(kp.areview(params=[
    ReviewParams(keys=ReviewField.PAGE, value=1),
    ReviewParams(keys=ReviewField.LIMIT, value=100)
]))
```

#### Sync

```python
from kinopoisk_dev import KinopoiskDev, ReviewParams, ReviewField

kp = KinopoiskDev(token=TOKEN)
item = kp.review(params=[
    ReviewParams(keys=ReviewField.PAGE, value=1),
    ReviewParams(keys=ReviewField.LIMIT, value=100)
])
```

### Person Awards

Награды актеров

- Ендпоинт - `/v1.1/person/awards`
- [Пример](./example/example_person_awards.py)

#### Async

```python
import asyncio
from kinopoisk_dev import KinopoiskDev, PersonAwardsField, PersonAwardsParams

kp = KinopoiskDev(token=TOKEN)
item = asyncio.run(await kp.aperson_awards(params=[
    PersonAwardsParams(keys=PersonAwardsField.PAGE, value=1),
    PersonAwardsParams(keys=PersonAwardsField.LIMIT, value=100),
]))
```

#### Sync

```python
from kinopoisk_dev import KinopoiskDev, PersonAwardsField, PersonAwardsParams

kp = KinopoiskDev(token=TOKEN)
item = kp.person_awards(params=[
    PersonAwardsParams(keys=PersonAwardsField.PAGE, value=1),
    PersonAwardsParams(keys=PersonAwardsField.LIMIT, value=100),
])
```

### Persons

- Ендпоинт - `/v1/person`
- [Пример](./example/example_person.py)

#### Async

```python
import asyncio
from kinopoisk_dev import KinopoiskDev, PersonParams, PersonField

kp = KinopoiskDev(token=TOKEN)
item = asyncio.run(kp.afind_many_person(params=[
    PersonParams(keys=PersonField.PAGE, value=1),
    PersonParams(keys=PersonField.LIMIT, value=100)
]))
```

#### Sync

```python
from kinopoisk_dev import KinopoiskDev, PersonParams, PersonField

kp = KinopoiskDev(token=TOKEN)
item = kp.find_many_person(params=[
    PersonParams(keys=PersonField.PAGE, value=1),
    PersonParams(keys=PersonField.LIMIT, value=100)
])
```

### Person

- Ендпоинт - `/v1/person/{id}`
- [Пример](./example/example_person_id.py)

#### Async

```python
import asyncio
from kinopoisk_dev import KinopoiskDev

kp = KinopoiskDev(token=TOKEN)
item = asyncio.run(kp.afind_one_person(24262))
```

#### Sync

```python
from kinopoisk_dev import KinopoiskDev

kp = KinopoiskDev(token=TOKEN)
item = kp.find_one_person(24262)
```

### Image

- Ендпоинт - `/v1/image`
- [Пример](./example/example_image.py)

#### Async

```python
import asyncio
from kinopoisk_dev import KinopoiskDev, ImageParams, ImageField

kp = KinopoiskDev(token=TOKEN)
item = asyncio.run(kp.aimage(params=[
    ImageParams(keys=ImageField.PAGE, value=1),
    ImageParams(keys=ImageField.LIMIT, value=100)
]))
```

#### Sync

```python
from kinopoisk_dev import KinopoiskDev, ImageParams, ImageField

kp = KinopoiskDev(token=TOKEN)
item = kp.image(params=[
    ImageParams(keys=ImageField.PAGE, value=1),
    ImageParams(keys=ImageField.LIMIT, value=100)
])

```