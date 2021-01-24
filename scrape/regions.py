from .classes import UndefinedRegion
from .noe import EuropeanRegion


# Regions from https://www.nintendo.com/regionselector/
REGIONS = [
    # -------- Americas --------
    UndefinedRegion('en_US', 'USA'),
    UndefinedRegion('en_CA', 'Canada (English)'),
    UndefinedRegion('fr_CA', 'Canada (French)'),
    UndefinedRegion('es_LA', 'México'),
    UndefinedRegion('pt_BR', 'Brasil'),
    UndefinedRegion('es_CO', 'Colombia'),
    UndefinedRegion('es_AR', 'Argentina'),
    UndefinedRegion('es_CL', 'Chile'),
    UndefinedRegion('es_PE', 'Perú'),
    # -------- Asia Pacific --------
    UndefinedRegion('ja_JP', 'Japan'),
    UndefinedRegion('ko_KR', 'Korea'),
    UndefinedRegion('zh_CN', 'China Mainland (Tencent)'),
    UndefinedRegion('zh_TW', 'Taiwan'),
    UndefinedRegion('zh_CH', 'Hong Kong'),
    UndefinedRegion('en_AU', 'Australia'),
    UndefinedRegion('en_NZ', 'New Zealand'),
    # -------- Europe, Middle East & Africa --------
    EuropeanRegion('de_AT', 'Austria', 'at'),
    EuropeanRegion('fr_BE', 'België (Dutch)', 'befr'),
    EuropeanRegion('nl_BE', 'Belgique (French)', 'denl'),
    EuropeanRegion('de_DE', 'Deutschland', 'de'),
    EuropeanRegion('es_ES', 'España', 'es'),
    EuropeanRegion('fr_FR', 'France', 'fr'),
    EuropeanRegion('it_IT', 'Italia', 'it'),
    EuropeanRegion('nl_NL', 'Nederland', 'nl'),
    EuropeanRegion('pt_PT', 'Portugal', 'pt'),
    EuropeanRegion('ru_RU', 'Russia', 'ru'),
    EuropeanRegion('en_ZA', 'South Africa', 'za'),
    EuropeanRegion('de_CH', 'Schweiz (German)', 'chde'),
    EuropeanRegion('fr_CH', 'Suisse (French)', 'chfr'),
    EuropeanRegion('it_CH', 'Svizzera (Italian)', 'chit'),
    EuropeanRegion('en_GB', 'UK & Ireland', 'en'),
    # ----
    UndefinedRegion('en_CZ', 'Czech Republic'),
    UndefinedRegion('en_DK', 'Denmark'),
    UndefinedRegion('en_FI', 'Finland'),
    UndefinedRegion('en_GR', 'Greece'),
    UndefinedRegion('en_HU', 'Hungary'),
    UndefinedRegion('he_IL', 'Israel'),
    UndefinedRegion('en_SE', 'Sweden'),
]
