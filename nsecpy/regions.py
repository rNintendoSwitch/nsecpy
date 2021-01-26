from dataclasses import dataclass

from .searchproviders import *


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
    Region('de_AT', 'Austria', WesternEuropeSearch('at')),
    Region('nl_BE', 'België (Dutch)', WesternEuropeSearch('benl')),
    Region('fr_BE', 'Belgique (French)', WesternEuropeSearch('befr')),
    Region('en_CZ', 'Czech Republic', CentralEuropeSearch('www.mojenintendo.cz')),
    Region('en_DK', 'Denmark', NordicSearch('www.nintendo.dk')),
    Region('de_DE', 'Deutschland', WesternEuropeSearch('de')),
    Region('es_ES', 'España', WesternEuropeSearch('es')),
    Region('en_FI', 'Finland', NordicSearch('www.nintendo.dk')),
    Region('fr_FR', 'France', WesternEuropeSearch('fr')),
    Region('en_GR', 'Greece', GreeceSearch()),
    Region('en_HU', 'Hungary', WesternEuropeSearch('www.nintendo.hu')),
    Region('he_IL', 'Israel', WesternEuropeSearch('www.nintendo.co.il')),
    Region('it_IT', 'Italia', WesternEuropeSearch('it')),
    Region('nl_NL', 'Nederland', WesternEuropeSearch('nl')),
    Region('pt_PT', 'Portugal', WesternEuropeSearch('pt')),
    Region('ru_RU', 'Russia', WesternEuropeSearch('ru')),
    Region('en_ZA', 'South Africa', WesternEuropeSearch('za')),
    Region('en_SE', 'Sweden', NordicSearch('www.nintendo.dk')),
    Region('de_CH', 'Schweiz (German)', WesternEuropeSearch('chde')),
    Region('fr_CH', 'Suisse (French)', WesternEuropeSearch('chfr')),
    Region('it_CH', 'Svizzera (Italian)', WesternEuropeSearch('chit')),
    Region('en_GB', 'UK & Ireland', WesternEuropeSearch('en')),
]
