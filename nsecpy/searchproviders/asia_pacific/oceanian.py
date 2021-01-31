import typing

from ..abcs import Game, SearchProvider


# TODO
class OceanianSearch(SearchProvider):
    def __init__(self):
        pass

    def search(self, query: typing.Union[str, int]) -> typing.Iterable[Game]:
        """Query can either be a search term (str) or nsuid (int)"""
        raise NotImplementedError()  # TODO
