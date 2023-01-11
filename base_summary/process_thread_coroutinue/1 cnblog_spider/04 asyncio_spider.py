# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 04 asyncio_spider
  Description : 协程 比 单线程更快，因为没有线程切换的开销
  Author      : chenyushencc@gmail.com
  date        : 2023/1/11 20:33
-------------------------------------------------
"""
import asyncio
import aiohttp
import blog_spider
import time


async def async_craw(url):
    print("craw url: ", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.text()
            print(f"craw url: {url}, {len(result)}")


loop = asyncio.get_event_loop()     # 至尊循环

tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls
]


if __name__ == "__main__":
    start = time.time()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print("used time ", end - start, " seconds")        # used time  0.8805069923400879  seconds

