from datetime import datetime
from typing import Any, List

from pydantic import BaseModel

from .page import Page


class Episode(BaseModel):
    number: int
    name: str = None
    enName: str=None
    description: Any
    date: datetime = None


class Doc(BaseModel):
    movieId: int
    number: int
    episodes: List[Episode]
    episodesCount: int


class Season(Page):
    docs: List[Doc]