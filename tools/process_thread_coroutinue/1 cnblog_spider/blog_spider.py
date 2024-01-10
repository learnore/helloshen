# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : blog_spider
  Description : 基础爬虫功能
  Author      : chenyushencc@gmail.com
  date        : 2023/1/11 10:34
-------------------------------------------------
"""
import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 51)
]


def craw(url):
    r = requests.get(url)
    return r.text


def parse(html):
    # class="post-item-title"
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]


if __name__ == "__main__":
    for result in parse(craw(urls[2])):     # urls[2] 第三页
        print(result)
