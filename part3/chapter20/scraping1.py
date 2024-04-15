import urllib.request
from urllib.parse import urljoin  # URLを扱うモジュールを追加
from bs4 import BeautifulSoup as BS


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BS(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "p-" not in url:
                continue
            print("\n" + url)

news = "https://gachi-matome.com/article-list-yugioh/"  # ニュース取得元サイトを変更
Scraper(news).scrape()
