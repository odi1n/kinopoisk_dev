from typing import Any


def get_params(params: Any) -> str:
    if not params:
        return ""
    return "&".join([param.__str__() for param in params])
