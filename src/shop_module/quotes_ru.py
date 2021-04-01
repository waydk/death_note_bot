import asyncio
import concurrent.futures

import requests
from bs4 import BeautifulSoup

URL = 'https://bbf.ru/quotes/?page=1&source=70405'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
           'accept': '*/*'}
quotes_ru = []


async def run_blocking_io(func, *args):
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, func, *args
        )
    return result


async def get_html(url, params):
    response = await run_blocking_io(requests.get, url, params)
    return response.text


async def get_content(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')
    items = soup.find_all('article', class_="sentence")
    page_quote = []
    for item in items:
        page_quote.append(
            f'{item.find("div", class_="sentence__character").get_text()}: '
            f' {item.find("div", class_="sentence__body").get_text()}')
    return page_quote


async def parse_quotes_ru():
    for i in range(1, 4):
        html = await get_html(URL.replace("?page=1", f'?page={i}'), params=HEADERS)
        quotes_ru.extend(await get_content(html))
    return quotes_ru
