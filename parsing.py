import requests
from bs4 import BeautifulSoup
import json

header = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.3'}
all_block = {}
for count in range(1, 8):
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
    response = requests.get(url, headers=header).text
    soup = BeautifulSoup(response, "lxml")
    blocks = soup.findAll("div", class_="w-full rounded border")
    for block in blocks:
        item_text = block.find("h4").text.strip()
        link = "https://scrapingclub.com" + block.find("a")["href"]
        price = block.find("h5").text.strip()
        url_img = "https://scrapingclub.com" + block.find("img", class_="card-img-top img-fluid").get("src")
        all_block[item_text] = {"link": link, "price": price, "img": url_img}

with open("all_categories.json", "w") as f:
    json.dump(all_block, f, indent=4)
