# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : auto_jd_beans
  Description : 1 京东官网地址：https://www.jd.com/
                2 pt_pin & pt_key ： https://github.com/learnore/helloshen/blob/main/base_summary/jpg/jd_pt.jpg

                1 进入腾讯控制台后，选中服务器，用“密码/密钥登录”，用 root 账户
                2 ps aux | grep "auto_jd_beans.py"
                3 kill -9 xxxxx
                4 编辑linux文本：
                        vim auto_jd_beans.py
                        点击按键 i
                        Esc 退出编辑
                        :wq 保存并退出
                5 nohup python auto_jd_beans.py > auto_jd_beans.log 2>&1 &

  Author      : chenyushencc@gmail.com
  date        : 2022/8/17 20:47
  copyright   : https://blog.csdn.net/qq_36624086/article/details/124222012
-------------------------------------------------
"""
import requests
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone='Asia/Shanghai')

pt_pin = "jd_540ff647c9d01"
pt_key = "xxxxx"


@sched.scheduled_job('cron', hour=6, minute=30)  # """ 每日 06:30 定时执行一次 """
def get_jd_beans():
    jd_beans_url = "https://api.m.jd.com/client.action?functionId=signBeanAct&body=%7B%22fp%22%3A%22-1%22%2C%22shshshfp%22%3A%22-1%22%2C%22shshshfpa%22%3A%22-1%22%2C%22referUrl%22%3A%22-1%22%2C%22userAgent%22%3A%22-1%22%2C%22jda%22%3A%22-1%22%2C%22rnVersion%22%3A%223.9%22%7D&appid=ld&client=apple&clientVersion=10.0.4&networkType=wifi&osVersion=14.8.1&uuid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&openudid=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6&jsonp=jsonp_1645885800574_58482";
    jd_beans_headers = {
        "Connection": 'keep-alive',
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cache-Control": 'no-cache',
        "User-Agent": "okhttp/3.12.1;jdmall;android;version/10.3.4;build/92451;",
        "accept": "*/*",
        "connection": "Keep-Alive",
        "Accept-Encoding": "gzip,deflate",
        "Cookie": "__jd_ref_cls=JingDou_SceneHome_NewGuidExpo;"
                  "mba_muid=1645885780097318205272.81.1645885790055;"
                  "mba_sid=81.5;"
                  "__jda=122270672.1645885780097318205272.1645885780.1645885780.1645885780.1;"
                  "__jdb=122270672.1.1645885780097318205272|1.1645885780;"
                  "__jdc=122270672;"
                  "__jdv=122270672%7Ckong%7Ct_1000170135%7Ctuiguang%7Cnotset%7C1644027879157;"
                  "pre_seq=0;"
                  "pre_session=3acd1f6361f86fc0a1bc23971b2e7bbe6197afb6|143;"
                  "unpl=JF8EAKZnNSttWRkDURtVThUWHAgEWw1dH0dXOjMMAFVcTQQAEwZORxR7XlVdXhRKFx9sZhRUX1NIVw4YBCsiEEpcV1ZVC0kVAV9XNVddaEpkBRwAExEZQ1lWW1kMTBcEaWcAUVpeS1c1KwUbGyB7bVFeXAlOFQJobwxkXGhJVQQZBR0UFU1bZBUzCQYXBG1vBl1VXElRAR8FGxUWS1hRWVsISCcBb2cHUm1b%7CV2_ZzNtbRYAFxd9DUNcKRxYB2ILGloRUUYcIVpAAHsbWQZjVBEJclRCFnUUR11nGlgUZgIZXkFcQRRFCEJkexhdB24LFFtEUHMQfQ5GXH0pXAQJbRZeLAcCVEULRmR6KV5VNVYSCkVVRBUiAUEDKRgMBTRREV9KUUNGdlxAByhNWwVvBUIKEVBzJXwJdlR6GF0GZAoUWUdRQCUpUBkCJE0ZWTVcIlxyVnMURUooDytAGlU1Vl9fEgUWFSIPRFN7TlUCMFETDUIEERZ3AEBUKBoIAzRQRlpCX0VFIltBZHopXA%253d%253d;"
                  "pt_key=" + pt_key + ";"
                  "pt_pin=" + pt_pin + ";"
                  "pwdt_id=jd_505bacd333f6b;"
                  "sid=1b2c8b7ce820c4188f048e689bf58c8w;"
                  "visitkey=36446698972455355"
    }

    response = requests.post(url=jd_beans_url, headers=jd_beans_headers)
    print("The Time is : %s" % datetime.now())
    print(response.text)


if __name__ == "__main__":
    sched.start()