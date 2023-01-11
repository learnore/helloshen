# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : lock_concurrent
  Description : 给线程加锁
  Author      : chenyushencc@gmail.com
  date        : 2023/1/11 12:16
-------------------------------------------------
"""
import threading
import time


lock = threading.Lock()


class Account:
    def __init__(self, balance):
        self.balance = balance


def draw_with_lock(account, amount):
    with lock:
        if account.balance >= amount:
            time.sleep(0.1)
            print(threading.current_thread().name, "取钱成功")
            account.balance -= amount
            print(threading.current_thread().name, "余额", account.balance)
        else:
            print(threading.current_thread().name, "余额不足，取钱失败")


if __name__ == "__main__":
    account = Account(1000)     # 账户有 1000 元
    t1 = threading.Thread(name="t1", target=draw_with_lock, args=(account, 800))      # 创建一个 t1 线程，取钱 800
    t2 = threading.Thread(name="t2", target=draw_with_lock, args=(account, 800))      # 创建一个 t2 线程，取钱 800
    t1.start()
    t2.start()

    # 只会出现一种情况 - 正常取钱
    """
    t1 取钱成功
    t1 余额 200
    t2 余额不足，取钱失败
    """