from typing import Any, Callable
from hashlib import md5


def build_hashkey(func: Callable, *args: Any, **kwargs: Any) -> str:
    return md5(kwargs.get("features").json().encode('utf-8')).hexdigest()

