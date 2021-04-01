import asyncio
import concurrent.futures

import requests
from bs4 import BeautifulSoup

URL = 'https://www.less-real.com/quotes/search/Death+Note?p=1'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
           'accept': '*/*'}
quotes = []


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
    items = soup.find_all('div', class_="quoteSmall")
    page_quote = []
    for item in items:
        page_quote.append(
            item.find("div", class_="quote").get_text().replace("(Death Note)", ""),
        )
    return page_quote


async def parse_quotes():
    for i in range(1, 7):
        html = await get_html(url=URL.replace("?p=1", f'?p={i}'), params=HEADERS)
        quotes.extend(await get_content(html))
    return quotes
