from __future__ import annotations
from collections.abc import Callable
from functools import wraps
from logging import getLogger
from typing import TypeVar, ParamSpec

P = ParamSpec("P")
T = TypeVar("T")

LOGGER = getLogger(__name__)


def retry(f: Callable[P, T]) -> Callable[P, T]:
    @wraps(f)
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        counter = 0
        while True:
            try:
                return f(*args, **kwargs)
            except Exception as e:
                LOGGER.error("Trying to suppress error", exc_info=e)
                counter += 1
                if counter == 3:
                    raise

    return inner
