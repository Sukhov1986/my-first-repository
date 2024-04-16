import requests
from bs4 import BeautifulSoup
import json


class Parser:
    base_url = 'https://habr.com'
    html = ""
    header = {"User-Agent":
                  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
              }
    res = {}

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        reg = requests.get(self.url, headers=self.header).text
        self.html = BeautifulSoup(reg, 'lxml')

    def parsing(self):
        news = self.html.findAll('article', class_='tm-articles-list__item')
        for item in news:
            try:
                title = item.find('a', class_='tm-title__link').text
            except AttributeError:
                title = "No title"
            try:
                autor = item.find('a', class_="tm-user-info__username").text.strip()
            except AttributeError:
                autor = 'No autor'
            try:
                href = self.base_url + item.find('h2').find('a').get('href')
            except AttributeError:
                href = 'No href'
            self.res[autor] = {
                'title': title,
                'href': href}

    def write_json(self):
        with open(self.path, 'a') as f:
            json.dump(self.res, f, indent=4)

    def run(self):
        self.get_html()
        self.parsing()
        self.write_json()
