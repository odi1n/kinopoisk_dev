from typing import Any, List

import grequests
import requests

from .exception import ApiFailedException, ApiUnauthenticated, ApiNotFound
from .field import Field


def get_request(link: str,
                params: dict = None) -> Any:
    response = requests.get(link, params=params)

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


def get_grequest(link: str, params: dict, field: Field, ids: List[str]):
    requests = (_grequest(link, params=params | {'field': field.value, 'search': id}) for id in ids)
    responses = grequests.map(requests)
    return responses


def _grequest(link: str,
              params: dict = None) -> Any:
    response = grequests.get(link, params=params)
    return response
