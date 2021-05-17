import copy

import pytest
from aioresponses import aioresponses

from nsecpy import UnsupportedRegionError, regions
from nsecpy.listing import COUNT

from .sample_data import SAMPLE_GAME


def build_sample_response_from_contents(contents, total=None, offset=0):
    assert offset % COUNT == 0

    if not total:
        total = len(contents)

    if (offset + COUNT) > total:
        length = total - offset
    else:
        length = COUNT

    return {"contents": contents, "length": length, "offset": offset, "total": total}


@pytest.mark.asyncio
async def test_listing_pagination():
    # Build Test Response
    page1_payload = build_sample_response_from_contents([SAMPLE_GAME] * COUNT, COUNT + 1, 0)
    page2_payload = build_sample_response_from_contents([SAMPLE_GAME], COUNT + 1, 30)

    with aioresponses() as m:
        m.get(f'https://ec.nintendo.com/api/US/en/search/ranking?offset=0&count={COUNT}', payload=page1_payload)
        m.get(f'https://ec.nintendo.com/api/US/en/search/ranking?offset={COUNT}&count={COUNT}', payload=page2_payload)

        lastGame = None
        gameCount = 0

        async for game in regions['en_US'].get_listing('ranking'):
            if lastGame:
                assert game == lastGame

            gameCount += 1
            lastGame = game

        assert gameCount == COUNT + 1


@pytest.mark.asyncio
async def test_listing_valid_types():
    # Build Test Response
    payload = build_sample_response_from_contents([SAMPLE_GAME], 1, 0)

    with aioresponses() as m:
        lastGame = None

        for type in ["sales", "new", "ranking"]:
            m.get(f'https://ec.nintendo.com/api/US/en/search/{type}?offset=0&count={COUNT}', payload=payload)

            async for game in regions['en_US'].get_listing(type):
                if lastGame:
                    assert game == lastGame


@pytest.mark.asyncio
async def test_listing_missing_images():
    # Build Test Response
    game = copy.deepcopy(SAMPLE_GAME)
    game['rating_info']['content_descriptors'][0].pop('image_url')
    game['rating_info']['content_descriptors'][0].pop('svg_image_url')
    game['rating_info']['rating'].pop('image_url')
    payload = build_sample_response_from_contents([game], 1, 0)

    with aioresponses() as m:
        m.get(f'https://ec.nintendo.com/api/US/en/search/ranking?offset=0&count={COUNT}', payload=payload)

        async for game in regions['en_US'].get_listing('ranking'):
            assert game


@pytest.mark.asyncio
async def test_listing_malformed_rating():
    # Build Test Response
    game = copy.deepcopy(SAMPLE_GAME)
    game['rating_info']['rating'] = {'id': 0}
    payload = build_sample_response_from_contents([game], 1, 0)

    with aioresponses() as m:
        m.get(f'https://ec.nintendo.com/api/US/en/search/ranking?offset=0&count={COUNT}', payload=payload)

        async for game in regions['en_US'].get_listing('ranking'):
            assert game


@pytest.mark.asyncio
async def test_listing_invalid_type():
    with pytest.raises(ValueError) as e_info:
        async for _ in regions['en_US'].get_listing('invalid_type_string'):
            pass


@pytest.mark.asyncio
async def test_listing_invalid_region():
    for region in regions.values():
        if not region.supports_listing:
            with pytest.raises(UnsupportedRegionError) as e_info:
                async for _ in region.get_listing('ranking'):
                    pass

            return

    raise RuntimeError('Failed to find region with no listing support')
