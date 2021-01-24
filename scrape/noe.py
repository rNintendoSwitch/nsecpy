from .classes import ScrapeRegion


ENDPOINT = 'https://searching.nintendo-europe.com/{solrLanguage}/select?q=*&start=0&rows=1000000&fq=(type:"game"AND((playable_on_txt%3A"HAC")))'


class EuropeanRegion(metaclass=ScrapeRegion):
    def __init__(self, cultureCode, familarName, solrLanguage):
        self.cultureCode = cultureCode
        self.familarName = familarName
        self.solrLanguage = solrLanguage
