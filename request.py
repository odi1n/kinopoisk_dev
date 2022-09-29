from typing import Any

# import grequests
import requests

from exception import ApiFailedException, ApiUnauthenticated, ApiNotFound


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
