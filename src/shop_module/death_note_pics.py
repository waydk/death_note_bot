import requests
from bs4 import BeautifulSoup

URL = 'https://wall.alphacoders.com/by_sub_category.php?id=172992&name=Death+Note+Wallpapers&page=1'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
           'accept': '*/*'}
pictures = []


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html_page):
    soup = BeautifulSoup(html_page, 'html.parser')
    items = soup.find_all('div', class_="thumb-container")
    page_images = []
    for item in items:
        page_images.append(
            item.find("img", class_="img-responsive").get("src")
        )
    return page_images


for i in range(1, 15):
    html = get_html(URL.replace("&page=1", f'?&page={i}')).text
    pictures.extend(get_content(html))