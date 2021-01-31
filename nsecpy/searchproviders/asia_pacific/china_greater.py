import typing

from ..abcs import Game, SearchProvider


# TODO: gets all data from https://{domain}/data/json/switch_software.json?281948944235=
class GreaterChinaSearch(SearchProvider):
    def __init__(self, domain):
        self.domain = domain

    def search(self, query: typing.Union[str, int]) -> typing.Iterable[Game]:
        """Query can either be a search term (str) or nsuid (int)"""
        raise NotImplementedError()  # TODO
