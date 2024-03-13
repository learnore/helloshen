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


if __name__ == "__main__":
    url_1 = "http://yjszs.nudt.edu.cn/index/index.view"  # 替换成你要检查的网站地址
    content_1 = get_website_content(url_1)

    if content_1:
        check_update(url_1, content_1)
    else:
        print("无法获取网站内容")
