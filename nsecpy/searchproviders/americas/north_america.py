import typing

from ..abcs import Game, SearchProvider


# TODO: Uses GraphQL @ graph.nintendo.com
class NorthAmericanSearch(SearchProvider):
    def __init__(self, locale):
        self.locale = locale

    def search(self, query: typing.Union[str, int]) -> typing.Iterable[Game]:
        """Query can either be a search term (str) or nsuid (int)"""
        raise NotImplementedError()  # TODO
