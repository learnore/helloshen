# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : thread_pool
  Description : 线程池
  Author      : chenyushencc@gmail.com
  date        : 2023/1/11 12:45
-------------------------------------------------
"""
import concurrent.futures
import blog_spider

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)        # pool.map 按顺序
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))
    print("craw over")

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    # for future, url in futures.items():       # 按顺序
    #     print(url, future.result())

    for future in concurrent.futures.as_completed(futures):     # 任务执行完了就马上返回
        url = futures[future]
        print(url, future.result())

