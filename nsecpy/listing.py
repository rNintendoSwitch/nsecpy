from dataclasses import dataclass, field
from datetime import datetime  # for typehinting
from typing import TYPE_CHECKING, Generator, List, Literal, Optional

import aiohttp


if TYPE_CHECKING:
    from nsecpy.regions import Region  # pragma: no cover


@dataclass
class ContentType:
    id: int = None
    name: str = None
    type: Literal["descriptor", "interactive"] = None
    image_url: Optional[str] = None  # JP Field
    svg_image_url: Optional[str] = None  # JP Field


@dataclass
class Rating:
    age: int = None
    id: int = None
    image_url: str = None
    name: str = None  # Literal["M", "T","10","e"] ??? expand and replace hint
    provisional: bool = None
    svg_image_url: str = None


@dataclass
class RatingSystem:
    id: int = None
    name: Literal["PEGI", "ESRB", "CERO"] = None


@dataclass
class Game:
    content_type: str = None
    dominant_colors: List[str] = None
    formal_name: str = None
    hero_banner_url: str = None
    id: str = None
    is_new: bool = None
    public_status: Literal["public"] = None
    rating_content: List[ContentType] = field(default_factory=list)
    rating: Rating = None
    rating_system: RatingSystem = None
    release_date_on_eshop: datetime = None
    screenshots: List[str] = field(default_factory=list)
    tags: List = field(default_factory=list)
    target_titles: List = field(default_factory=list)


async def fetchListing(region: "Region", type: Literal["sales", "new", "ranking"]) -> Generator[List[Game], None, None]:
    COUNT = 30

    # TODO: Check if (all) regions support this endpoint?

    if type not in ["sales", "new", "ranking"]:
        raise ValueError("invalid type: " + type)

    lang, reg = region.culture_code.split('_')
    offset = 0

    async with aiohttp.ClientSession() as session:
        while True:
            url = f'https://ec.nintendo.com/api/{reg}/{lang}/search/{type}?offset={offset}&count={COUNT}'

            async with session.get(url) as request:
                request.raise_for_status()
                data = await request.json()

                for game in data['contents']:
                    yield game  # TODO: Parse

                if (offset + COUNT) >= data['total']:
                    break

            offset += COUNT
