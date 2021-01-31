import typing

from ..abcs import Game, SearchProvider


# TODO: Uses https://www.nintendoswitch.com.cn/api/web/official_website/query_software_game_list?limit=8&offset=8
class MainlandChinaSearch(SearchProvider):
    def __init__(self):
        pass

    def search(self, query: typing.Union[str, int]) -> typing.Iterable[Game]:
        """Query can either be a search term (str) or nsuid (int)"""
        raise NotImplementedError()  # TODO
