import datetime
from dataclasses import dataclass, field
from typing import Dict, List, Literal, Optional


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
    release_date_on_eshop: datetime.datetime = None
    screenshots: List[str] = field(default_factory=list)
    tags: List = field(default_factory=list)
    target_titles: List = field(default_factory=list)
