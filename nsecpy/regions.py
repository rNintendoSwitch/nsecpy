from dataclasses import dataclass

from .searchproviders import (
    SearchProvider,
    EuropeSearch,
    NorthAmericanSearch,
    SouthAmericanSearch,
    JapanSearch,
    KoreanSearch,
    MainlandChinaSearch,
    GreaterChinaSearch,
    OceanianSearch,
)


@dataclass
class Region:
    cultureCode: str
    familarName: str
    searchProvider: SearchProvider


# Regions from https://www.nintendo.com/regionselector/
regions = [
    # -------- Americas --------
    Region('en_US', 'USA', NorthAmericanSearch('en_US')),
    Region('en_CA', 'Canada (English)', NorthAmericanSearch('en_CA')),
    Region('fr_CA', 'Canada (French)', NorthAmericanSearch('fr_CA')),
    Region('es_LA', 'México', NorthAmericanSearch('es_LA')),
    Region('pt_BR', 'Brasil', SouthAmericanSearch('store.nintendo.com.br')),
    Region('es_CO', 'Colombia', SouthAmericanSearch('store.nintendo.co')),
    Region('es_AR', 'Argentina', SouthAmericanSearch('store.nintendo.com.ar')),
    Region('es_CL', 'Chile', SouthAmericanSearch('store.nintendo.cl')),
    Region('es_PE', 'Perú', SouthAmericanSearch('store.nintendo.com.pe')),
    # -------- Asia Pacific --------
    Region('ja_JP', 'Japan', JapanSearch()),
    Region('ko_KR', 'Korea', KoreanSearch()),
    Region('zh_CN', 'China Mainland (Tencent)', MainlandChinaSearch()),
    Region('zh_TW', 'Taiwan', GreaterChinaSearch('www.nintendo.tw')),
    Region('zh_CH', 'Hong Kong', GreaterChinaSearch('www.nintendo.com.hk')),
    Region('en_AU', 'Australia', OceanianSearch()),
    Region('en_NZ', 'New Zealand', OceanianSearch()),
    # -------- Europe, Middle East & Africa --------
    Region('de_AT', 'Austria', EuropeSearch('at')),
    Region('nl_BE', 'België (Dutch)', EuropeSearch('benl')),
    Region('fr_BE', 'Belgique (French)', EuropeSearch('befr')),
    Region('en_CZ', 'Czech Republic'),
    Region('en_DK', 'Denmark'),
    Region('de_DE', 'Deutschland', EuropeSearch('de')),
    Region('es_ES', 'España', EuropeSearch('es')),
    Region('en_FI', 'Finland'),
    Region('fr_FR', 'France', EuropeSearch('fr')),
    Region('en_GR', 'Greece'),
    Region('en_HU', 'Hungary'),
    Region('he_IL', 'Israel'),
    Region('it_IT', 'Italia', EuropeSearch('it')),
    Region('nl_NL', 'Nederland', EuropeSearch('nl')),
    Region('pt_PT', 'Portugal', EuropeSearch('pt')),
    Region('ru_RU', 'Russia', EuropeSearch('ru')),
    Region('en_ZA', 'South Africa', EuropeSearch('za')),
    Region('en_SE', 'Sweden'),
    Region('de_CH', 'Schweiz (German)', EuropeSearch('chde')),
    Region('fr_CH', 'Suisse (French)', EuropeSearch('chfr')),
    Region('it_CH', 'Svizzera (Italian)', EuropeSearch('chit')),
    Region('en_GB', 'UK & Ireland', EuropeSearch('en')),
]
