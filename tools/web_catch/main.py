# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : main
  Description : 启动程序
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/3/13 10:31
-------------------------------------------------
"""
from tools.web_catch.web_catch import get_website_content, check_update


""" 链接和 class 配置 """
link_class = [
    {
        "name": "研招网-空军工程大学",
        "url": "https://yz.chsi.com.cn/sch/schoolInfo--schId-368547.dhtml",
        "class": "yxk-column-con"           # 调剂 class
    },
    {
        "name": "国防科技大学官网",
        "url": "http://yjszs.nudt.edu.cn/index/index.view",
        "class": "tzgg"
    }
]


if __name__ == "__main__":
    for key, value in enumerate(link_class):
        print(key, value, value["name"], value["url"], value["class"])

        name, url, catch_class = value["name"], value["url"], value["class"]
        content = get_website_content(url, catch_class)
        if content:
            check_update(name, url, catch_class, content)
        else:
            print(name + " 无法获取网站内容")
