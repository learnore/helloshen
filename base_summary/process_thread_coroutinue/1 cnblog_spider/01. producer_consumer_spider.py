# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 01. producer_consumer_spider
  Description : Python 实现生产者消费者爬虫
                B站 - https://www.bilibili.com/video/BV1bK411A7tV?p=5&vd_source=3b789929c119fbb870018b0c617f79f8

  Author      : chenyushencc@gmail.com
  date        : 2023/1/11 11:48
-------------------------------------------------
"""
import queue
import random
import threading
import time

import blog_spider


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.craw(url)
        html_queue.put(html)
        print(
            threading.current_thread().name, f"craw {url}",
            "url_queue.size = ", url_queue.qsize()
        )
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, my_file):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for result in results:
            my_file.write(str(result) + "\n")
        print(
            threading.current_thread().name, f"results.size = ", len(results),
            "html_queue.size = ", html_queue.qsize()
        )
        time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in blog_spider.urls:
        url_queue.put(url)

    for idx in range(3):        # 3 个生产者
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f"craw{idx}")
        t.start()

    my_file = open("01. producer_consumer_spider.txt", "w")
    for idx in range(2):        # 2 个消费者
        t = threading.Thread(target=do_parse, args=(html_queue, my_file), name=f"parse{idx}")
        t.start()


