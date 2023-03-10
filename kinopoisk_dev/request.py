from typing import Any

import requests
import httpx

from .exception import ApiFailedException, ApiNotFound, ApiUnauthenticated
from .abc import RequestABC


class Request(RequestABC):
    def get(self, link: str, params: dict = None) -> Any:
        with httpx.Client() as client:
            response = client.get(
                link,
                params=params,
                headers=self._headers
            )

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            raise ApiUnauthenticated(response.status_code, response.text)
        elif response.status_code == 404:
            raise ApiNotFound(response.status_code, response.text)
        elif response.status_code == 500:
            raise ApiFailedException(response.status_code, response.text)
        else:
            raise Exception(response.status_code, response.text)


class AsyncRequest(RequestABC):
    async def get(self, link: str, params: dict = None) -> Any:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                link,
                params=params,
                headers=self._headers
            )

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            raise ApiUnauthenticated(response.status_code, response.text)
        elif response.status_code == 404:
            raise ApiNotFound(response.status_code, response.text)
        elif response.status_code == 500:
            raise ApiFailedException(response.status_code, response.text)
        else:
            raise Exception(response.status_code, response.text)
