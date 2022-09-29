from pydantic import BaseModel


class Page(BaseModel):
    total: int
    limit: int
    page: int
    pages: int
