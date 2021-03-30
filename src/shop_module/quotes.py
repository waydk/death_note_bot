import requests
from bs4 import BeautifulSoup

URL = 'https://www.less-real.com/quotes/search/Death+Note?p=1'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
           'accept': '*/*'}
quotes = []


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')
    items = soup.find_all('div', class_="quoteSmall")
    page_quote = []
    for item in items:
        page_quote.append(
            item.find("div", class_="quote").get_text().replace("(Death Note)", ""),
        )
    return page_quote


for i in range(1, 7):
    html = get_html(URL.replace("?p=1", f'?p={i}')).text
    quotes.extend(get_content(html))
