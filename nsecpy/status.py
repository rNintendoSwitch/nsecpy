from dataclasses import dataclass
from datetime import datetime  # for typehinting
from enum import Enum
from typing import TYPE_CHECKING, Dict, List, Optional

import aiohttp
import dateparser


if TYPE_CHECKING:
    from nsecpy.regions import Region


class EventStatus(Enum):
    PLANNED = 0
    IDENTIFED = 1  # a guess?
    ONGOING = 2  # a guess?
    ENDED = 3


class PlatformTypeEnum(Enum):
    NORMAL = 0
    OFFLINE = 1


@dataclass
class PlatformStatus:
    name: str = None
    type: PlatformTypeEnum = None

    def __init__(self, data: Dict) -> None:
        self.name = data.get('name')
        self.type = PlatformTypeEnum(data.get('type'))


@dataclass
class PlatformOutage:
    platform: List[str] = None
    platform_image = None
    software_title: str = None
    message: str = None
    free_write: str = None
    begin: datetime = None
    end: datetime = None
    utc_del_time: Optional[datetime] = None
    event_status: EventStatus = None
    services: List[str] = None
    update_date: Optional[datetime] = None

    def __init__(self, data, region: "Region") -> None:
        self.platform = data['platform']
        self.platform_image = data['platform_image']
        self.software_title = data['software_title']
        self.message = data['message']
        self.free_write = data['free_write']
        self.begin = dateparser.parse(
            data['begin'].replace(' :', ':'),
            settings={'TIMEZONE': region.netinfo_TZ, 'RETURN_AS_TIMEZONE_AWARE': True},
        )
        self.end = dateparser.parse(
            data['end'].replace(' :', ':'),
            settings={'TIMEZONE': region.netinfo_TZ, 'RETURN_AS_TIMEZONE_AWARE': True},
        )
        if data.get('utc_del_time'):
            self.utc_del_time = dateparser.parse(
                data['utc_del_time'].replace(' :', ':'),
                settings={'TIMEZONE': region.netinfo_TZ, 'RETURN_AS_TIMEZONE_AWARE': True},
            )
        self.event_status = EventStatus(int(data['event_status']))
        self.services = data.get('services', [])
        self


@dataclass
class Status:
    lang: str
    categories: List[PlatformStatus] = None
    operational_statuses: List[PlatformOutage] = None
    temporary_maintenances: List[PlatformOutage] = None

    def __init__(self, data: dict, region: "Region") -> None:
        self.lang = data.get('lang')
        self.operational_statuses = [PlatformOutage(each, region) for each in data.get('operational_statuses')]
        self.categories = [PlatformStatus(each) for each in data.get('categories')]
        self.temporary_maintenances = [PlatformOutage(each, region) for each in data.get('temporary_maintenances')]


async def getStatus(region: "Region") -> Status:
    if not region.has_netinfo:
        raise ValueError("region has no netinfo")
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://www.nintendo.co.jp/netinfo/{region.culture_code}/status.json") as request:
            request.raise_for_status()
            data = await request.json()
            return Status(data, region=region)
