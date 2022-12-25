from typing import TypeVar

import requests
from requests.models import Response
from retrying import retry

from loguru_learn.log import logger


@logger.catch
@retry(stop_max_attempt_number=3)
def get(url: str) -> Response:
    resp = requests.get(url=url)
    return resp


# logger.exception("123")

get("www.baidu.com")
