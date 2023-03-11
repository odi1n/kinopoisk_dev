from typing import Generic, TypeVar, Union

T = TypeVar("T")


class BaseParams(Generic[T]):
    keys: Union[str, T]
    value: str

    def __init__(
        self,
        keys: Union[str, T],
        value: str,
    ):
        self.keys = keys
        self.value = value

    def __str__(self):
        if isinstance(self.keys, str):
            return f"{self.keys}={self.value}"
        return f"{self.keys.value}={self.value}"
