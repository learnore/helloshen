# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : main
  Description : 启动程序

                暂不支持名单整理
                · B站(要验证)

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/3/13 10:31
-------------------------------------------------
"""
import asyncio

from tools.web_catch.web_catch import get_website_content, check_update


""" 链接和 class 配置 """
link_class = [
    # 国防科技大学 985
    {
        "name": "国防科技大学官网-通知公告",
        "url": "http://yjszs.nudt.edu.cn/index/index.view",
        "class": "tzgg"
    },
    {
        "name": "国防科技大学官网-院所发文",
        "url": "http://yjszs.nudt.edu.cn/index/index.view",
        "class": "kswd zcfg fr"
    },
    {
        "name": "国防科技大学官网-首页模块",
        "url": "http://yjszs.nudt.edu.cn/index/index.view",
        "class": "zcfg fl"
    },
    {
        "name": "研招网-国防科技大学",
        "url": "https://yz.chsi.com.cn/sch/schoolInfo--schId-368388.dhtml",
        "class": "left"
    },

    # 西南大学 211 重庆
    {
        "name": "西南大学-官网-最新动态",
        "url": "http://yz.swu.edu.cn/s/yanzhao/",
        "class": "index-2-2 col-right"
    },
    {
        "name": "研招网-西南大学",
        "url": "https://yz.chsi.com.cn/sch/schoolInfo--schId-368457.dhtml",
        "class": "left"
    },

    # 中国矿业大学(北京) 211
    {
        "name": "中国矿业大学-官网-硕士招生",
        "url": "https://yz.cumt.edu.cn/index/sszs/14.htm",
        "class": "ny_right"
    },
    {
        "name": "研招网-中国矿业大学(北京)",
        "url": "https://yz.chsi.com.cn/sch/schoolInfo--schId-367923.dhtml",
        "class": "left"
    },
    {
        "name": "研招网-中国矿业大学(苏州)",
        "url": "https://yz.chsi.com.cn/sch/schoolInfo--schId-368184.dhtml",
        "class": "left"
    },

    # 江南大学 211
    {
        "name": "江南大学-官网-最新通知",     # TODO 法获取网站内容
        "url": "https://yz.jiangnan.edu.cn/",
        "class": "notice_list"
    },
    {
        "name": "研招网-江南大学",
        "url": "https://yz.chsi.com.cn/sch/schoolInfo--schId-368189.dhtml",
        "class": "left"
    },


    # 南京农业大学 211
    {
        "name": "南京农业大学-官方",
        "url": "https://zsgz.njau.edu.cn/zsxx/sszs/sszxtz.htm",
        "class": "pull-right list-right"
    },
    {
        "name": "研招网-南京农业大学",
        "url": "https://yz.chsi.com.cn/sch/schoolInfo--schId-368198.dhtml",
        "class": "left"
    },


    # 信息工程大学
    {
        "name": "研招网-信息工程大学(河南郑州)",
        "url": "https://yz.chsi.com.cn/sch/listBulletin--schId-368312,categoryId-462794,mindex-10.dhtml",
        "class": "container"           # 调剂 class
    },

    # 空军工程大学
    {
        "name": "研招网-空军工程大学",
        "url": "https://yz.chsi.com.cn/sch/schoolInfo--schId-368547.dhtml",
        "class": "yxk-column-con"           # 调剂 class
    },

    # test
    {
        "name": "CSDN-头条",
        "url": "https://www.csdn.net/",
        "class": "headlines-right"
    },
]


async def main():
    tasks = []
    # 创建任务并启动多个协程
    for key, value in enumerate(link_class):
        # print(key, value, value["name"], value["url"], value["class"])
        name, url, catch_class = value["name"], value["url"], value["class"]
        content = get_website_content(url, catch_class)
        if content:
            task = asyncio.create_task(check_update(name, url, catch_class, content))
            tasks.append(task)

        else:
            print(name + " 无法获取网站内容")

    for task in tasks:
        await task


if __name__ == "__main__":
    # 运行主协程
    asyncio.run(main())
