from enum import Enum


class SeasonField(Enum):
    SELECT_FIELDS = "selectFields"
    SORT_FIELD = "sortField"
    SORT_TYPE = "sortType"
    PAGE = "page"
    LIMIT = "limit"
    MOVIE_ID = "movieId"
    NUMBER = "number"
    EPISODES_COUNT = "episodesCount"
    EPISODES_MOVIE_ID = "episodes.movieId"
    EPISODES_SEASON_NUMBER = "episodes.seasonNumber"
    EPISODES_EPISODE_NUMBER = "episodes.episodeNumber"
    EPISODES_NAME = "episodes.name"
    EPISODES_ALTERNATIVE_NAME = "episodes.alternativeName"
    EPISODES_DESCRIPTION = "episodes.description"
    EPISODES_DATE = "episodes.date"
