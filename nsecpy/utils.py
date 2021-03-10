from math import ceil
from typing import Generator, Iterable, TypeVar


_T = TypeVar("_T")


def grouper(iterable: Iterable[_T], n: int) -> Generator[Iterable[_T], None, None]:
    """
    given a iterable, yield that iterable back in chunks of size n. last item will be any size.
    """
    for i in range(ceil(len(iterable) / n)):
        yield iterable[i * n : i * n + n]
