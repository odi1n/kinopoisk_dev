from enum import Enum


class ReviewField(Enum):
    SELECT_FIELDS = "selectFields"
    SORT_FIELD = "sortField"
    SORT_TYPE = "sortType"
    PAGE = "page"
    LIMIT = "limit"
    ID = "id"
    MOVIE_ID = "movieId"
    TITLE = "title"
    TYPE = "type"
    REVIEW = "review"
    DATE = "date"
    AUTHOR = "author"
    AUTHOR_ID = "authorId"
