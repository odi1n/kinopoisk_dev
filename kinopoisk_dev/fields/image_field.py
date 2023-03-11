from enum import Enum


class ImageField(Enum):
    SELECT_FIELDS = "selectFields"
    SORT_FIELD = "sortField"
    SORT_TYPE = "sortType"
    PAGE = "page"
    LIMIT = "limit"
    MOVIE_ID = "movieId"
    TYPE = "type"
    LANGUAGE = "language"
    URL = "url"
    PREVIEW_URL = "previewUrl"
    HEIGHT = "height"
    WIDTH = "width"
