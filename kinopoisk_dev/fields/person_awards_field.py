from enum import Enum


class PersonAwardsField(Enum):
    SELECT_FIELDS = "selectFields"
    SORT_FIELD = "sortField"
    SORT_TYPE = "sortType"
    PAGE = "page"
    LIMIT = "limit"
    NOMINATION_AWARD_TITLE = "nomination.award.title"
    NOMINATION_AWARD_YEAR = "nomination.award.title"
    NOMINATION_TITLE = "nomination.award.title"
    WINNING = "winning"
    PERSON_ID = "personId"
    MOVIE_ID = "movie.id"
    MOVIE_NAME = "movie.name"
    MOVIE_RATING = "movie.rating"
