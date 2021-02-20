from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List


@dataclass
class PlatformStatus:
    name: str
    type: int  # turn into an enum at some point?


class EventStatus(Enum):
    DISCOVERED = 1  # this is a guess.
    IDENTIFIED = 2  # this is a guess.
    ENDED = 3


@dataclass
class PlatformOutage:
    platform: List[str] = field(default_factory=list)
    platform_image = field(default_factory=list)
    software_title: str = None
    message: str = None
    begin: datetime = None
    end: datetime = None
    utc_del_time: datetime = None
    event_status: EventStatus = None
    services: List[str] = field(default_factory=list)
    update_date: datetime = None


@dataclass
class Status:
    lang: str
    categories: List[PlatformStatus] = field(default_factory=list)
    operational_statuses: List = field(default_factory=list)
    temporary_maintenances: List[PlatformOutage] = field(default_factory=list)
