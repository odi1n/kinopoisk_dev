import abc
from typing import Any, Dict, Optional

from httpx import Response


class RequestABC(abc.ABC):
    def __init__(self, token: str):
        self._headers = {
            "Accept": "application/json",
            "Accept-Encoding": "identity",
            "X-API-KEY": token,
        }

    @abc.abstractmethod
    def get(self, link: str, params: Optional[Dict[str, Any]] = None) -> Response:
        pass
