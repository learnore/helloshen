# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : web_catch
  Description : 根据网页的 class 捕捉网页信息
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/3/13 10:04
-------------------------------------------------
"""
import requests
import datetime
import asyncio

from bs4 import BeautifulSoup
from send_email import set_email


def get_website_content(url, catch_class):
    # 发送HTTP请求获取网页内容
    response = requests.get(url)

    if response.status_code == 200:
        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 这里假设网站内容是放在<div class="content">标签内的
        content_tag = soup.find('div', class_=catch_class)

        if content_tag:
            return content_tag.get_text()

    return None


async def check_update(name, url, catch_class, last_content):
    # 每隔一段时间检查一次网站更新
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")      # 记录当前时间

        new_content = get_website_content(url, catch_class)
        if new_content and new_content != last_content:
            print(f"{now} {name} 网站有更新！\n {new_content}")
            # 存入文本 并发送邮件提醒
            with open("dedails.txt", "w", encoding='utf-8') as file:
                file.write(new_content)
            set_email()

            last_content = new_content
        else:
            # print(f"point {name} \n {new_content}")
            print(f"{now} 网站暂无更新 {name}")

        await asyncio.sleep(60)  # 间隔60秒再次检查


async def test_email():
    """ 每隔一段时间，发送 test 邮件，观测程序在运行 """
    while True:
        set_email()
        print("Web Catch start~\nGood news is coming~")

        await asyncio.sleep(7200)  # 间隔2小时秒再次检查


if __name__ == "__main__":
    name = "监测网站名称"
    url = "https://news.cctv.com/"  # 替换成你要检查的网站地址
    catch_class = "content"
    last_content = get_website_content(url, catch_class)
    if last_content:
        check_update(url, catch_class, last_content)
    else:
        print(name + " 无法获取网站内容")

