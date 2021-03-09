from dataclasses import dataclass, field
from datetime import datetime
from os import execlp  # for typehinting
from typing import TYPE_CHECKING, List, Literal, Optional

import aiohttp
import dateparser

if TYPE_CHECKING:
    from nsecpy.regions import Region  # pragma: no cover


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
        self.start = dateparser.parse(data['start_datetime'], settings={'TIMEZONE': "UTC"})
        self.end = dateparser.parse(data['end_datetime'], settings={'TIMEZONE': "UTC"})
        super().__init__(data)


@dataclass
class PriceQuery:
    sales_status: Literal["onsale"]
    title_id: int
    regular_price: Price
    discount_price: Optional[DiscountPrice] = None

    def __init__(self, data) -> None:
        self.sales_status = data['sales_status']
        self.title_id = data['title_id']
        self.regular_price = Price(data['regular_price'])
        if data.get('discount_price'):
            self.discount_price = DiscountPrice(data['discount_price'])


### Sample Responses:
#
# {
#     "personalized": false,
#     "country": "JP",
#     "prices": [
#         {
#             "title_id": 70010000009922,
#             "sales_status": "onsale",
#             "regular_price": {"amount": "1,620円", "currency": "JPY", "raw_value": "1620"},
#         }
#     ],
# }
# {
#     "personalized": false,
#     "country": "US",
#     "prices": [
#         {
#             "title_id": 70010000039205,
#             "sales_status": "onsale",
#             "regular_price": {"amount": "$3.99", "currency": "USD", "raw_value": "3.99"},
#             "discount_price": {
#                 "amount": "$2.99",
#                 "currency": "USD",
#                 "raw_value": "2.99",
#                 "start_datetime": "2021-03-06T10:00:00Z",
#                 "end_datetime": "2021-03-26T15:59:59Z",
#             },
#         }
#     ],
# }


class NoResultError(Exception):
    pass


async def priceQuery(region: "Region", game_id: int) -> PriceQuery:
    # TODO: Check what regions this supports

    lang, reg = region.culture_code.split('_')
    url = f"https://api.ec.nintendo.com/v1/price?country={reg}&lang={lang}&ids={game_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as request:
            request.raise_for_status()
            data = await request.json()

            if 'prices' in data and data['prices']:
                return PriceQuery(data['prices'][0])
            else:
                return NoResultError('The API did not find price info for given game id')