import pytest
from aioresponses import aioresponses

from nsecpy import regions, UnsupportedRegionError
from .sample_data import SAMPLE_STATUS_EN, SAMPLE_STATUS_DE


@pytest.mark.asyncio
async def test_status_equality():
    with aioresponses() as m:
        m.get('https://www.nintendo.co.jp/netinfo/en_US/status.json', payload=SAMPLE_STATUS_EN)
        m.get('https://www.nintendo.co.jp/netinfo/de_DE/status.json', payload=SAMPLE_STATUS_DE)

        en_status = await regions['en_US'].getStatus()
        de_status = await regions['de_DE'].getStatus()

        # Correct langs
        assert en_status.lang == 'en_US'
        assert de_status.lang == 'de_DE'

        # Assert categories are equal
        assert en_status.categories == de_status.categories

        # Assert operational_statuses and temporary_maintenances are equivalent temporary_maintenances
        for outage_group in [
            (en_status.operational_statuses, de_status.operational_statuses),
            (en_status.temporary_maintenances, de_status.temporary_maintenances),
        ]:
            en_outages, de_outages = outage_group
            assert len(en_outages) == len(de_outages)

            for i in range(len(en_outages)):
                en, de = en_outages[i], de_outages[i]

                # Asserts for existance
                for attr in ['software_title', 'message', 'free_write', 'services', 'update_date']:
                    assert hasattr(en, attr)
                    assert hasattr(de, attr)

                # Asserts for fields that should equal
                assert en.platform == de.platform
                assert en.platform_image == de.platform_image
                assert en.event_status == de.event_status
                assert en.event_status == de.event_status
                assert en.begin == en.begin
                assert en.end == de.end
                if hasattr(en, 'utc_del_time'):
                    assert en.utc_del_time == de.utc_del_time

                # update_date is not given with a time, so we can only 'eh' it with timezones, that they are +/- 2 days
                if hasattr(en, 'update_date'):
                    delta = en.update_date - de.update_date
                    assert abs(delta.total_seconds()) < 60 * 60 * 24 * 2


@pytest.mark.asyncio
async def test_status_invalid_region():
    for region in regions.values():
        if not region.netinfo_TZ:
            with pytest.raises(UnsupportedRegionError) as e_info:
                await region.getStatus()

            return

    raise RuntimeError('Failed to find region with no netinfo')
