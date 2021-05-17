from dataclasses import dataclass
from typing import Generator, List, Literal, Optional, Union

from .listing import Game, query_listing
from .pricing import PriceQuery, query_price, query_prices
from .status import Status, query_status


@dataclass
class Region:
    culture_code: str
    familar_name: str
    # search_provider: SearchProvider = None
    supports_listing: bool = True
    supports_pricing: bool = True
    netinfo_TZ: Optional[str] = None

    async def query_status(self) -> Status:
        return await query_status(self)

    async def query_listing(self, type: Literal["sales", "new", "ranking"]) -> Generator[Game, None, None]:
        async for game in query_listing(self, type):
            yield game

    async def query_price(self, game: Union[int, "Game"]) -> PriceQuery:
        return await query_price(self, game)

    async def query_prices(self, games: List[Union[int, "Game"]]) -> Generator[PriceQuery, None, None]:
        async for game in query_prices(self, games):
            yield game


# Regions from https://www.nintendo.com/regionselector/
regions_list = [
    # -------- Americas --------
    Region('en_US', 'USA', netinfo_TZ="America/Los_Angeles"),
    Region('en_CA', 'Canada (English)'),
    Region('fr_CA', 'Canada (French)', netinfo_TZ="America/Toronto"),
    Region('es_MX', 'México', netinfo_TZ="America/Los_Angeles"),
    Region('pt_BR', 'Brasil', netinfo_TZ="America/Los_Angeles"),
    Region('es_CO', 'Colombia'),
    Region('es_AR', 'Argentina'),
    Region('es_CL', 'Chile'),
    Region('es_PE', 'Perú'),
    # # -------- Asia Pacific --------
    Region('ja_JP', 'Japan', netinfo_TZ="Asia/Tokyo"),
    Region('ko_KR', 'Korea', netinfo_TZ="Asia/Seoul"),
    Region('zh_CN', 'China Mainland (Tencent)', netinfo_TZ="Asia/Shanghai", supports_listing=False),
    Region('zh_TW', 'Taiwan', netinfo_TZ="Asia/Taipei", supports_listing=False, supports_pricing=False),
    Region('zh_HK', 'Hong Kong'),
    Region('en_AU', 'Australia', netinfo_TZ="Australia/Sydney"),
    Region('en_NZ', 'New Zealand'),
    # -------- Europe, Middle East & Africa --------
    Region('de_AT', 'Austria'),
    Region('nl_BE', 'België (Dutch)'),
    Region('fr_BE', 'Belgique (French)'),
    Region('en_CZ', 'Czech Republic'),
    Region('en_DK', 'Denmark'),
    Region('de_DE', 'Deutschland', netinfo_TZ="Europe/Berlin"),
    Region('es_ES', 'España', netinfo_TZ="Europe/Madrid"),
    Region('en_FI', 'Finland'),
    Region('fr_FR', 'France', netinfo_TZ="Europe/Paris"),
    Region('en_GR', 'Greece'),
    Region('en_HU', 'Hungary'),
    Region('he_IL', 'Israel', supports_listing=False),
    Region('it_IT', 'Italia', netinfo_TZ="Europe/Rome"),
    Region('nl_NL', 'Nederland', netinfo_TZ="Europe/Amsterdam"),
    Region('pt_PT', 'Portugal', netinfo_TZ="Europe/Lisbon"),
    Region('ru_RU', 'Russia', netinfo_TZ="Europe/Moscow"),
    Region('en_ZA', 'South Africa'),
    Region('en_SE', 'Sweden'),
    Region('de_CH', 'Schweiz (German)'),
    Region('fr_CH', 'Suisse (French)'),
    Region('it_CH', 'Svizzera (Italian)'),
    Region('en_GB', 'UK & Ireland', netinfo_TZ="Europe/London"),
]

# Comprehend list into dict, indexed by culture code
regions = {r.culture_code: r for r in regions_list}
