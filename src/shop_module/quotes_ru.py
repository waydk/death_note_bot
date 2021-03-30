import requests
from bs4 import BeautifulSoup

URL = 'https://bbf.ru/quotes/?page=1&source=70405'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
           'accept': '*/*'}
quotes_ru = []


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')
    items = soup.find_all('article', class_="sentence")
    page_quote = []
    for item in items:
        page_quote.append(
            f'{item.find("div", class_="sentence__character").get_text()}: '
            f' {item.find("div", class_="sentence__body").get_text()}')
    return page_quote


for i in range(1, 4):
    html = get_html(URL.replace("?page=1", f'?page={i}')).text
    quotes_ru.extend(get_content(html))


