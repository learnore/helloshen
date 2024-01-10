# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : lock_concurrent
  Description : 未加锁，线程随机出现 BUG
  Author      : chenyushencc@gmail.com
  date        : 2023/1/11 12:16
-------------------------------------------------
"""
import threading
import time


class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    if account.balance >= amount:
        time.sleep(0.1)  # 如果没有time.sleep 会进行线程切换，所以加上这句，一定会复现 BUG
        print(threading.current_thread().name, "取钱成功")
        account.balance -= amount
        print(threading.current_thread().name, "余额", account.balance)
    else:
        print(threading.current_thread().name, "余额不足，取钱失败")


if __name__ == "__main__":
    account = Account(1000)     # 账户有 1000 元
    t1 = threading.Thread(name="t1", target=draw, args=(account, 800))      # 创建一个 t1 线程，取钱 800
    t2 = threading.Thread(name="t2", target=draw, args=(account, 800))      # 创建一个 t2 线程，取钱 800
    t1.start()
    t2.start()

    """ 可能出现的情况 """

    # 情况 1
    """
    t1 取钱成功
    t1 余额 200
    t2 余额不足，取钱失败
    """

    # 情况 2
    """
    t1 取钱成功
    t2t1 余额 200
    取钱成功
    t2 余额 -600
    """
