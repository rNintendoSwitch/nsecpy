import asyncio
from os import execlp
import pytest

from aioresponses import aioresponses
from nsecpy import regions


SAMPLE_STATUS_EN = {
    "lang": "en_US",
    "categories": [
        {"name": "Wii U", "type": 0},
        {"name": "nintendo 3DS", "type": 0},
        {"name": "Wii", "type": 0},
        {"name": "nintendo DS", "type": 0},
        {"name": "web", "type": 0},
        {"name": "other", "type": 0},
        {"name": "iOS", "type": 0},
        {"name": "Nintendo Switch", "type": 0},
        {"name": "Android", "type": 0},
    ],
    "operational_statuses": [
        {
            "platform": ["web"],
            "platform_image": ["img/label_web.png"],
            "software_title": "Purchasing on Nintendo Game Store",
            "message": "During the times specified below, we experienced technical difficulties with our network service. \nAt this time, the network service is back up and running. \nWe apologize for any inconvenience this may have caused.",
            "free_write": "",
            "begin": "Monday, January 22, 2018  2 :14 AM",
            "end": "Monday, January 22, 2018  3 :07 AM",
            "utc_del_time": "2018-01-23 03:07:00",
            "event_status": "0",
            "services": ["All network services"],
            "update_date": "Monday, January 22, 2018",
        }
    ],
    "temporary_maintenances": [
        {
            "platform": ["Nintendo Switch"],
            "platform_image": ["img/label_switch.png"],
            "software_title": "Online play of some software",
            "message": "Server maintenance has been completed. Thank you for your cooperation.",
            "free_write": "",
            "begin": "Wednesday, February 24, 2021  6 :55 AM",
            "end": "Wednesday, February 24, 2021  7 :01 AM",
            "utc_del_time": "2021-02-25 15:01:00",
            "event_status": "3",
            "services": ["certain network services"],
            "update_date": "Wednesday, February 24, 2021",
        },
        {
            "platform": ["Nintendo Switch"],
            "platform_image": ["img/label_switch.png"],
            "software_title": "Network Services",
            "message": "During the maintenance window, network services may be unavailable.",
            "free_write": "",
            "begin": "Wednesday, February 24, 2021  8 :30 PM",
            "end": "Wednesday, February 24, 2021 11 :30 PM",
            "event_status": "0",
            "services": ["Notice to friends, etc."],
            "update_date": "Tuesday, February 23, 2021",
        },
    ],
}


SAMPLE_STATUS_DE = {
    "lang": "de_DE",
    "categories": [
        {"name": "Wii U", "type": 0},
        {"name": "nintendo 3DS", "type": 0},
        {"name": "Wii", "type": 0},
        {"name": "nintendo DS", "type": 0},
        {"name": "web", "type": 0},
        {"name": "other", "type": 0},
        {"name": "iOS", "type": 0},
        {"name": "Nintendo Switch", "type": 0},
        {"name": "Android", "type": 0},
    ],
    "operational_statuses": [
        {
            "platform": ["web"],
            "platform_image": ["img/label_web.png"],
            "software_title": "Kauf im Nintendo Game Store",
            "message": "Während der unten angegebenen Zeiten hatten wir technische Probleme mit unserem Netzwerkdienst. \nZu diesem Zeitpunkt ist der Netzwerkdienst wieder aktiv. \nWir entschuldigen uns für etwaige Unannehmlichkeiten. ",
            "free_write": "",
            "begin": "Montag, 22. Januar 2018, 11:14 Bin",
            "end": "Montag, 22. Januar 2018, 12:07 Uhr",
            "utc_del_time": "2018-01-23 03:07:00",
            "event_status": "0",
            "services": ["Alle Netzwerkdienste"],
            "update_date": "Montag, 22. Januar 2018",
        }
    ],
    "temporary_maintenances": [
        {
            "platform": ["Nintendo Switch"],
            "platform_image": ["img/label_switch.png"],
            "software_title": "Online-Spiel für einige Software-Titel",
            "message": "Die Wartungsarbeiten am Server sind abgeschlossen. Vielen Dank für deine Geduld.",
            "free_write": "",
            "begin": "Mittwoch, 24. Februar 2021, 15:55 Uhr",
            "end": "Mittwoch, 24. Februar 2021, 16:01 Uhr",
            "utc_del_time": "2021-02-25 15:01:00",
            "event_status": "3",
            "services": ["bestimmte Netzdienste"],
            "update_date": "Mittwoch, 24. Februar 2021",
        },
        {
            "platform": ["Nintendo Switch"],
            "platform_image": ["img/label_switch.png"],
            "software_title": "Online-Services",
            "message": "Während des angegebenen Zeitraums führen wir Wartungsarbeiten am Server durch. Unsere Online-Services sind dann möglicherweise nicht verfügbar.",
            "free_write": "",
            "begin": "Donnerstag, 25. Februar 2021,  5:30 Uhr",
            "end": "Donnerstag, 25. Februar 2021,  8:30 Uhr",
            "event_status": "0",
            "services": ["Freundesmitteilungen, etc."],
            "update_date": "Mittwoch, 24. Februar 2021",
        },
    ],
}


def test_status_equality():
    loop = asyncio.get_event_loop()
    with aioresponses() as m:
        m.get('https://www.nintendo.co.jp/netinfo/en_US/status.json', payload=SAMPLE_STATUS_EN)
        m.get('https://www.nintendo.co.jp/netinfo/de_DE/status.json', payload=SAMPLE_STATUS_DE)

        en_status = loop.run_until_complete(regions['en_US'].getStatus())
        de_status = loop.run_until_complete(regions['de_DE'].getStatus())

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
            for i in range(len(outage_group[0])):
                en, de = outage_group[0][i], outage_group[1][i]

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


def test_status_invalid_region():
    for region in regions.values():
        if not region.has_netinfo:
            with pytest.raises(ValueError) as e_info:
                loop = asyncio.get_event_loop()
                status = loop.run_until_complete(region.getStatus())

            return
    raise RuntimeError('Failed to find region with no netinfo')