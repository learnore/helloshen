# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : main
  Description : 启动程序

                暂不支持名单整理
                1、 B站(要验证)


  Summary     : 准备环境
                1、pip install beautifulsoup4
                2、git clone https://github.com/learnore/helloshen.git       # 克隆 github 项目（也可以不克隆整个项目，个人随意）
                3、修改邮件授权码

                常用命令
                1、rm -rf helloshen      # 删除整个文件夹且不用逐一询问
                   cd ali_shen/my_workspace/helloshen/tools/web_catch
                2、git stash             # 将未提交的更改保存在一个临时的存储区中
                   git pull             # 拉取新代码
                   git stash pop        # 恢复暂存的更改
                3、nohup python web_catch_main.py > web_catch_main.log 2>&1 &
                4、ps aux | grep "web_catch_main.py"
                  kill -9 xxxxx


  Author      : chenyushencc@gmail.com
  date        : 2024/3/13 10:31
-------------------------------------------------
"""
import asyncio
import logging

from my_logging import LoggerWriter
from web_catch import get_website_content, check_update, test_email

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

    # 空军军医大学 211
    {
        "name": "空军军医大学-官网-院系通知",
        "url": "https://www.fmmu.edu.cn/tongzhi/yxtz/yjsy1.htm",
        "class": "jgtz"
    },
    {
        "name": "研招网-空军军医大学",
        "url": "https://yz.chsi.com.cn/sch/schoolInfo--schId-368546.dhtml",
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


    # 研究所，信息主要来源 = 研招网 + 微信公众号 + 官网
    # 武汉邮电科学研究院
    {
        "name": "研招网-武汉邮电科学研究院 + 关注公众号",
        "url": "https://yz.chsi.com.cn/sch/schoolInfo--schId-368331.dhtml",
        "class": "left"  # 调剂 class
    },

    # 中国兵器科学研究院(西南自动化研究所)
    {
        "name": "研招网-中国兵器科学研究院(西南自动化研究所) + 关注公众号",
        "url": "https://yz.chsi.com.cn/sch/schoolInfo--schId-368469.dhtml",
        "class": "left"  # 调剂 class
    },

    # 研究院-中国地震局地震研究所
    {
        "name": "研招网-中国地震局地震研究所",
        "url": "https://yz.chsi.com.cn/sch/schoolInfo--schId-368329.dhtml",
        "class": "left"  # 调剂 class
    },
    {
        "name": "中国地震局地震研究所-官网",
        "url": "https://www.ief.ac.cn/zstext/index.html",
        "class": "secondarybox"  # 调剂 class
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
    # 创建一个定时发送官方邮件的 test 邮件
    task = asyncio.create_task(test_email())
    tasks.append(task)

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
    # 将 sys.stdout 和 sys.stderr 重定向到日志记录器
    """ 将 print 打印成日志，需要本地打印时，注释掉 """
    import sys
    sys.stdout = LoggerWriter(logging.INFO)
    sys.stderr = LoggerWriter(logging.ERROR)
    """ 将 print 打印成日志，需要本地打印时，注释掉 """

    # 运行主协程
    asyncio.run(main())
