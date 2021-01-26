import typing

from . import Game, SearchProvider


# TODO: Uses https://search.nintendo.jp/nintendo_soft/search.json?opt_hard=1_HAC&limit=300&page=1
class JapanSearch(metaclass=SearchProvider):
    def __init__(self):
        pass

    def search(self, query: typing.Union[str, int]) -> typing.Iterable[Game]:
        """Query can either be a search term (str) or nsuid (int)"""
        raise NotImplementedError()  # TODO
