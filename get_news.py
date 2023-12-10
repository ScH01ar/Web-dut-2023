import requests
from bs4 import BeautifulSoup
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63',
}


def get_news(url):
    path = url.split('/')[-1]
    path = url.replace(path, "")
    res = requests.get(url, headers=headers).content.decode("utf-8")
    html = BeautifulSoup(res, "html.parser")
    main_part = html.find_all("div", class_="cn-main")[0]
    title = main_part.find("p", class_="cn-main-title").text
    date = main_part.find("span", class_="info-date").text
    content_html = str(main_part.find_all(
        "div", class_="TRS_Editor")[1]).replace("./", path)
    News = {"title": title, "date": date, "content": content_html}
    with open("./health/static/news/2.json", "w", encoding="utf-8")as f:
        json.dump(News, f, ensure_ascii=False)
        f.close()


def get_newslist(url):
    res = requests.get(url, headers=headers).content.decode("utf-8")
    html = BeautifulSoup(res, "html.parser")
    main_part = html.find_all("div", class_="cn-item")
    newslist = []
    for item in main_part:
        img = url+item.find("img")['src']
        link = url+item.find("div", class_="item-title").find("a")['href']
        title = item.find("div", class_="item-title").find("a").text
        dic = {"title": title, "img": img, "link": link}
        newslist.append(dic)
    with open("./health/static/news/news_list.json", "w", encoding="utf-8")as f:
        json.dump(newslist, f, ensure_ascii=False)
        f.close()


# get_news("https://www.chinacdc.cn/yyrdgz/202302/t20230214_263727.html")
get_newslist("https://www.chinacdc.cn/yyrdgz/")
