from dataclasses import dataclass, field
from datetime import datetime
from os import execlp  # for typehinting
from typing import TYPE_CHECKING, List, Literal, Optional

import aiohttp
import dateparser

from .exceptions import NoDataError, NotFoundError, UnsupportedRegionError


if TYPE_CHECKING:
    from .regions import Region  # pragma: no cover


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
    sales_status: Literal["onsale", "sales_termination"]
    title_id: int
    regular_price: Price
    discount_price: Optional[DiscountPrice] = None

    def __init__(self, data) -> None:
        if data['sales_status'] == 'not_found':
            raise NotFoundError('The API reported no price info was found in this region for given game id')

        self.sales_status = data['sales_status']
        self.title_id = data['title_id']
        self.regular_price = Price(data['regular_price'])
        if data.get('discount_price'):
            self.discount_price = DiscountPrice(data['discount_price'])


async def queryPrice(region: "Region", game_id: int) -> PriceQuery:
    if not region.supports_pricing:
        raise UnsupportedRegionError("Region does not support listings")

    lang, reg = region.culture_code.split('_')
    url = f"https://api.ec.nintendo.com/v1/price?country={reg}&lang={lang}&ids={game_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as request:
            request.raise_for_status()
            data = await request.json()

            if 'prices' in data and data['prices']:
                return PriceQuery(data['prices'][0])
            else:
                raise NoDataError('The API did not return any price data for given game id')
