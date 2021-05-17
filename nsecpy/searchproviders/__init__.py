class SearchProvider:
    async def search_by_nsuid(self, nsuid: str) -> ...:
        raise NotImplementedError("this SearchProvider does not support this method")

    async def search_by_query(self, query: str) -> ...:
        raise NotImplementedError("this SearchProvider does not support this method")
