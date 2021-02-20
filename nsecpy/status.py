from nsecpy.regions import Region
import aiohttp
from .classes import Status


async def getStatus(region: Region) -> Status:
    if not region.has_netinfo:
        raise ValueError("region has no netinfo")
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://www.nintendo.co.jp/netinfo/{region.culture_code}/status.json") as request:
            request.raise_for_status()
            data = await request.json()
            return Status(data, region=region)