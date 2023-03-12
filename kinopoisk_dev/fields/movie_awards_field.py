from enum import Enum


class MovieAwardsField(Enum):
    SELECT_FIELDS = "selectFields"
    SORT_FIELD = "sortField"
    SORT_TYPE = "sortType"
    PAGE = "page"
    LIMIT = "limit"
    ID = "id"
    NOMINATION_AWARD_TITLE = "nomination.award.title"
    NOMINATION_AWARD_YEAR = "nomination.award.title"
    NOMINATION_TITLE = "nomination.award.title"
    WINNING = "winning"
    MOVIE_ID = "movieId"
