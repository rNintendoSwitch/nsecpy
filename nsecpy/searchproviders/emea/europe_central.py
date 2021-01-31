import typing

from ..abcs import Game, SearchProvider


# TODO
class CentralEuropeSearch(SearchProvider):
    def __init__(self, domain):
        self.domain = domain

    def search(self, query: typing.Union[str, int]) -> typing.Iterable[Game]:
        """Query can either be a search term (str) or nsuid (int)"""
        raise NotImplementedError()  # TODO
