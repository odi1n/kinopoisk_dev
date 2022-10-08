from typing import Union

from ..field import Field


class SeasonParams:
    field: Union[str, Field]
    search: str

    def __init__(self,
                 field: Union[str, Field] = None,
                 search: str = None):
        self.field = field
        self.search = search

    def __str__(self):
        link = ""
        if self.field is not None:
            link += f'field[]={self.field.value}' if isinstance(self.field, Field) else f'field[]={self.field}'
        if self.search is not None:
            link += f'&search[]={self.search}'
        return link
