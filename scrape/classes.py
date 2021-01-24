import abc
import typing


class Game:
    pass


class ScrapeRegion(metaclass=abc.ABCMeta):
    def __init__(self, cultureCode, familarName):
        self.cultureCode = cultureCode
        self.familarName = familarName

    @abc.abstractmethod
    def scrape(self) -> typing.Iterable[Game]:
        pass


class UndefinedRegion(metaclass=ScrapeRegion):
    pass
