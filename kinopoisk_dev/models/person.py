from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel

from .page import Page


class Fact(BaseModel):
    value: str


class Movie(BaseModel):
    id: int
    name: Optional[str]
    rating: Optional[float]
    general: bool
    description: str


class ProfessionItem(BaseModel):
    value: str


class Person(BaseModel):
    spouses: List
    id: int
    __v: int
    age: int
    birthPlace: List
    birthday: str
    countAwards: int
    createdAt: str
    death: Any
    deathPlace: List
    enName: str
    facts: List[Fact]
    growth: int
    movies: List[Movie]
    name: str
    photo: str
    profession: List[ProfessionItem]
    sex: str
    updatedAt: str


class PersonList(Page):
    docs: List[Movie]
