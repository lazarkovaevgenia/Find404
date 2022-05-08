
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


SITE = 'https://typeurlhere.com'
visited = []

def find404(url, parent):
    if url in visited:
        return
    else:
        visited.append(url)
    print('url=', url)
    try:
        html = get_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.select('a')
        for element in elements:
            if not element.has_attr('href'):
                continue
            href = element['href']
            if href.startswith('.') or href.startswith('#'):
                continue
            href = urljoin(url, href)
            print('href=', href)
            if href.startswith(SITE):
                find404(href, url)


    except ResourceWarning:
        print('Битая ссылка', url, 'на странице', parent)


def get_html(url):
    response = requests.get(url)
    if response.status_code == 404:
        raise ResourceWarning()
    return response.text


if __name__ == '__main__':
    find404(SITE, SITE)

