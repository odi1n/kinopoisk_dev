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

#### Async

```python
import asyncio
from kinopoisk_dev import KinopoiskDev, PossValField

kp = KinopoiskDev(token=TOKEN)
item = asyncio.run(kp.apossible_values_by_field(poss_val_field=PossValField.GENRES))
```

#### Sync

```python
from kinopoisk_dev import KinopoiskDev, PossValField

kp = KinopoiskDev(token=TOKEN)
item = kp.possible_values_by_field(poss_val_field=PossValField.GENRES)
```