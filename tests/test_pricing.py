import copy
import pytest
from aioresponses import aioresponses

from nsecpy import regions, NotFoundError, NoDataError, UnsupportedRegionError
from nsecpy.listing import Game
from .sample_data import SAMPLE_GAME, SAMPLE_PRICE_RESPONSE


@pytest.mark.asyncio
async def test_pricing_sane_datatime():
    with aioresponses() as m:
        url = 'https://api.ec.nintendo.com/v1/price?country=US&lang=en&ids=70010000039205'
        m.get(url, payload=SAMPLE_PRICE_RESPONSE)

        price = await regions['en_US'].queryPrice(70010000039205)

        assert price.discount_price.end > price.discount_price.start


@pytest.mark.asyncio
async def test_pricing_from_game():
    with aioresponses() as m:
        # Build response without diffrent title id
        response = copy.deepcopy(SAMPLE_PRICE_RESPONSE)
        response['prices'][0]['title_id'] = 70010000036098

        m.get('https://api.ec.nintendo.com/v1/price?country=US&lang=en&ids=70010000036098', payload=response)

        game = Game(SAMPLE_GAME, regions['en_US'])
        price = await game.queryPrice()

        assert price


@pytest.mark.asyncio
async def test_pricing_compare_discount():
    with aioresponses() as m:
        DISCOUNT_ID = 70010000039205
        NORMAL_ID = 7001000012345
        URL_BASE = 'https://api.ec.nintendo.com/v1/price?country=US&lang=en&ids='

        # Build Response without discount
        normal_response = copy.deepcopy(SAMPLE_PRICE_RESPONSE)
        normal_response['prices'][0].pop('discount_price')
        normal_response['prices'][0]['title_id'] = NORMAL_ID

        m.get(URL_BASE + str(DISCOUNT_ID), payload=SAMPLE_PRICE_RESPONSE)
        m.get(URL_BASE + str(NORMAL_ID), payload=normal_response)

        discount = await regions['en_US'].queryPrice(DISCOUNT_ID)
        normal = await regions['en_US'].queryPrice(NORMAL_ID)

        assert normal.sales_status == discount.sales_status
        assert normal.regular_price == discount.regular_price
        assert normal.title_id == NORMAL_ID
        assert discount.title_id == DISCOUNT_ID
        assert discount.discount_price


@pytest.mark.asyncio
async def test_pricing_not_found():
    with aioresponses() as m:
        # Build not_found response data
        response = copy.deepcopy(SAMPLE_PRICE_RESPONSE)
        response['prices'][0].pop('regular_price')
        response['prices'][0].pop('discount_price')
        response['prices'][0]['sales_status'] = 'not_found'

        m.get('https://api.ec.nintendo.com/v1/price?country=US&lang=en&ids=70010000039205', payload=response)

        with pytest.raises(NotFoundError) as e_info:
            await regions['en_US'].queryPrice(70010000039205)


@pytest.mark.asyncio
async def test_pricing_no_data():
    with aioresponses() as m:
        # Build not_found response data
        response = copy.deepcopy(SAMPLE_PRICE_RESPONSE)
        response['prices'].pop(0)

        m.get('https://api.ec.nintendo.com/v1/price?country=US&lang=en&ids=70010000039205', payload=response)

        with pytest.raises(NoDataError) as e_info:
            await regions['en_US'].queryPrice(70010000039205)


@pytest.mark.asyncio
async def test_pricing_invalid_region():
    for region in regions.values():
        if not region.supports_pricing:
            with pytest.raises(UnsupportedRegionError) as e_info:
                await region.queryPrice(70010000039205)

            return

    raise RuntimeError('Failed to find region with no pricing support')