from dataclasses import dataclass, field
from datetime import datetime
from os import execlp  # for typehinting
from typing import TYPE_CHECKING, List, Literal, Optional

import aiohttp
import dateparser

from .exceptions import NoDataError, NotFoundError, UnsupportedRegionError


if TYPE_CHECKING:
    from .regions import Region  # pragma: no cover
    from nsecpy.listing import Game


@dataclass
class Price:
    amount: str = None
    currency: str = None
    raw_value: str = None

    def __init__(self, data) -> None:
        self.amount = data['amount']
        self.currency = data['currency']
        self.raw_value = data['raw_value']


@dataclass
class DiscountPrice(Price):
    start: datetime = None
    end: datetime = None

    def __init__(self, data) -> None:
        tzsettings = {'TIMEZONE': 'UTC', 'RETURN_AS_TIMEZONE_AWARE': True}
        self.start = dateparser.parse(data['start_datetime'], settings=tzsettings)
        self.end = dateparser.parse(data['end_datetime'], settings=tzsettings)
        super().__init__(data)


@dataclass
class PriceQuery:
    region: "Region" = None
    sales_status: Literal["onsale", "sales_termination"] = None
    title_id: int = None
    regular_price: Price = None
    discount_price: Optional[DiscountPrice] = None

    def __init__(self, data, region) -> None:
        if data['sales_status'] == 'not_found':
            raise NotFoundError('The API reported no price info was found in this region for given game id')

        self.region = region
        self.sales_status = data['sales_status']
        self.title_id = data['title_id']
        self.regular_price = Price(data['regular_price'])
        if data.get('discount_price'):
            self.discount_price = DiscountPrice(data['discount_price'])


async def queryPrice(region: "Region", game_id: int) -> PriceQuery:
    if not region.supports_pricing:
        raise UnsupportedRegionError("Region does not support pricing")

    lang, reg = region.culture_code.split('_')
    url = f"https://api.ec.nintendo.com/v1/price?country={reg}&lang={lang}&ids={game_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as request:
            request.raise_for_status()
            data = await request.json()

            if 'prices' in data and data['prices']:
                return PriceQuery(data['prices'][0], region)
            else:
                raise NoDataError('The API did not return any price data for given game id')


async def attachPrices(games: List["Game"], region: "Region") -> List["Game"]:
    if not region.supports_pricing:
        raise UnsupportedRegionError("Region does not support pricing")

    if len(games) > 50:
        raise ValueError("too many arguments; 50 at most")

    lang, reg = region.culture_code.split('_')
    ids = ','.join([str(game.id) for game in games])
    url = f"https://api.ec.nintendo.com/v1/price?country={reg}&lang={lang}&ids={ids}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as request:
            request.raise_for_status()
            data = await request.json()
            prices = data['prices']
            ret = []
            for game in games:
                value = next((price for price in prices if price['title_id'] == game.id), None)
                if value:
                    pd = PriceQuery(value, region)
                game._price = pd
                ret.append(game)
            return ret