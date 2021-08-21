from typing import Any, Callable
from hashlib import md5


def build_hashkey(func: Callable, *args: Any, **kwargs: Any) -> str:
    return md5(str(kwargs.get("features")).encode()).hexdigest()
