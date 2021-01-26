import abc
import typing
from dataclasses import dataclass

from .europe import *
from .americas import *
from .asia_pacific import *

# TODO: Move this to another file and do something with it
@dataclass
class Game:
    pass


class SearchProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def search(self, query: typing.Union[str, int]) -> typing.Iterable[Game]:
        """Query can either be a search term (str) or nsuid (int)"""
        pass
