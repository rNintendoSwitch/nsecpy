from . import SearchProvider, Game
import typing

# TODO: ENDPOINT = 'https://searching.nintendo-europe.com/{solrLanguage}/select?q=*&start=0&rows=1000000&fq=(type:"game"AND((playable_on_txt%3A"HAC")))'
class EuropeSearch(metaclass=SearchProvider):
    def __init__(self, solrLanguage):
        self.solrLanguage = solrLanguage

    def search(self, query: typing.Union[str, int]) -> typing.Iterable[Game]:
        """Query can either be a search term (str) or nsuid (int)"""
        raise NotImplementedError()  # TODO
