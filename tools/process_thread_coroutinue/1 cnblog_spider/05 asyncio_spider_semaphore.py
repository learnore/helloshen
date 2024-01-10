# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 05 asyncio_spider_semaphore
  Description : 异步 IO 中使用信号量（Semaphore）控制协程
  Author      : chenyushencc@gmail.com
  date        : 2023/1/11 21:14
-------------------------------------------------
"""
import asyncio
import aiohttp
import blog_spider
import time


semaphore = asyncio.Semaphore(10)       # 限制 10 个协程并发执行


async def async_craw(url):
    """ 方法一  async with semaphore """
    """
    async with semaphore:
    print("craw url: ", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.text()
            # await time.sleep(5)
            print(f"craw url: {url}, {len(result)}")
    """

    # ---------------------------------------------------
    """ 方法二 
    await semaphore.acquire()
    try:
        # TODO 
    finally:
        semaphore.release()
    """
    await semaphore.acquire()
    try:
        print("craw url: ", url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                result = await response.text()
                # await time.sleep(5)
                print(f"craw url: {url}, {len(result)}")
    finally:
        semaphore.release()


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
