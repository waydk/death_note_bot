import asyncio
import concurrent.futures

import requests

pictures = []

URL = "https://wallhaven.cc/api/v1/search"


async def run_blocking_io(func, *args):
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, func, *args
        )
    return result


async def get(url, params):
    response = await run_blocking_io(requests.get, url, params)
    return response.json()


async def parse_pictures():
    for page in range(1, 5):
        parameters = {
            "q": "death note",
            "page": f"{page}",
        }
        data = await get(url=URL, params=parameters)
        for photo in data['data']:
            pictures.append(photo["path"])
    return pictures
