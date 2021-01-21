from aiohttp import ClientSession


ENDPOINT = 'https://searching.nintendo-europe.com/{0}/select?q=*&start=0&rows=1000000&fq=(type:"game"AND((playable_on_txt%3A"HAC")))'
REGIONS = [
    'at',  # Austria - de_AT
    'befr',  # Belgium / Belgique (French) - fr_BE
    'benl',  # Belgium / België (Dutch) - nl_BE
    'chde',  # Switzerland / Schweiz (German) - de_CH
    'chfr',  # Switzerland / Suisse (French) - fr_CH
    'chit',  # Switzerland / Svizzera (Italian) - it_CH
    'de',  # Germany / Deutschland - de_DE
    'en',  # UK & Ireland - en_GB
    'es',  # Spain / España - es_ES
    'fr',  # France - fr_FR
    'it',  # Italy / Italia - it_IT
    'nl',  # Netherlands / Nederland - nl_NL
    'pt',  # Portugal - pt_PT
    'ru',  # Russian - ru_RU
    'za',  # South Africa - en_ZA
]
