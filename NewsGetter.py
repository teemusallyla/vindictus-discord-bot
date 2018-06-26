import requests
from bs4 import BeautifulSoup
import json

base_url = "http://vindictus.nexon.net/news/all/"
news = {"news": []}
for x in range(1, 4):
    print(x)
    url = base_url + str(x)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        news_raw = soup.find_all("div", class_ = "news-list-item")
        for news_piece in news_raw:
            news_item = {}
            news_item["title"] = news_piece.find(class_ = "news-list-item-title").text.replace("\r", "").replace("\n", "").replace("\t", "").replace("  ", "")
            news_item["content"] = news_piece.find(class_ = "news-list-item-text").text.replace("\r", "").replace("\n", "").replace("\t", "").replace("  ", "")
            news_item["link"] = "http://vindictus.nexon.net" + news_piece.find(class_ = "news-list-link").get("href")
            news["news"].append(news_item)


news["news"] = news["news"][:25]
with open("news.json", "w+") as f:
    json.dump(news, f)

    
