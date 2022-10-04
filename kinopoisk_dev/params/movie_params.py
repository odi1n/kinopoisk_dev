from typing import Union

from ..field import Field


class MovieParams:
    field: Union[str, Field]
    search: str
    sortField: str = None
    sortType: int = None

    def __init__(self,
                 field: Union[str, Field] = None,
                 search: str = None,
                 sortField: str = None,
                 sortType: int = None):
        self.field = field
        self.search = search
        self.sortField = sortField
        self.sortType = sortType

    def __str__(self):
        link = ""
        if self.field is not None:
            link += f'field[]={self.field.value}' if isinstance(self.field, Field) else f'field[]={self.field}'
        if self.search is not None:
            link += f'&search[]={self.search}'
        if self.sortField is not None:
            link += f'&sortField={self.sortField}'
        if self.sortType is not None:
            link += f'&sortType={self.sortType}'
        return link
