from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel

from .page import Page


class Episode(BaseModel):
    number: int
    name: Optional[str]
    enName: Optional[str]
    description: Any
    date: Optional[datetime]


class Doc(BaseModel):
    movieId: int
    number: int
    episodes: List[Episode]
    episodesCount: int


class Season(Page):
    docs: List[Doc]
