from dataclasses import dataclass

from .searchproviders.abcs import SearchProvider


@dataclass
class Region:
    culture_code: str
    familar_name: str
    search_provider: SearchProvider = None
    has_netinfo: bool = False  # https://www.nintendo.co.jp/netinfo/xx_XX/status.json


# Regions from https://www.nintendo.com/regionselector/
regions = [
    # -------- Americas --------
    Region('en_US', 'USA', has_netinfo=True),
    Region('en_CA', 'Canada (English)'),
    Region('fr_CA', 'Canada (French)', has_netinfo=True),
    Region('es_LA', 'México'),
    Region('pt_BR', 'Brasil', has_netinfo=True),
    Region('es_CO', 'Colombia'),
    Region('es_AR', 'Argentina'),
    Region('es_CL', 'Chile'),
    Region('es_PE', 'Perú'),
    # -------- Asia Pacific --------
    Region('ja_JP', 'Japan', has_netinfo=True),
    Region('ko_KR', 'Korea', has_netinfo=True),
    Region('zh_CN', 'China Mainland (Tencent)', has_netinfo=True),
    Region('zh_TW', 'Taiwan', has_netinfo=True),
    Region('zh_CH', 'Hong Kong'),
    Region('en_AU', 'Australia', has_netinfo=True),
    Region('en_NZ', 'New Zealand'),
    # -------- Europe, Middle East & Africa --------
    Region('de_AT', 'Austria'),
    Region('nl_BE', 'België (Dutch)'),
    Region('fr_BE', 'Belgique (French)'),
    Region('en_CZ', 'Czech Republic'),
    Region('en_DK', 'Denmark'),
    Region('de_DE', 'Deutschland', has_netinfo=True),
    Region('es_ES', 'España', has_netinfo=True),
    Region('en_FI', 'Finland'),
    Region('fr_FR', 'France', has_netinfo=True),
    Region('en_GR', 'Greece'),
    Region('en_HU', 'Hungary'),
    Region('he_IL', 'Israel'),
    Region('it_IT', 'Italia', has_netinfo=True),
    Region('nl_NL', 'Nederland', has_netinfo=True),
    Region('pt_PT', 'Portugal', has_netinfo=True),
    Region('ru_RU', 'Russia', has_netinfo=True),
    Region('en_ZA', 'South Africa'),
    Region('en_SE', 'Sweden'),
    Region('de_CH', 'Schweiz (German)'),
    Region('fr_CH', 'Suisse (French)'),
    Region('it_CH', 'Svizzera (Italian)'),
    Region('en_GB', 'UK & Ireland', has_netinfo=True),
]
