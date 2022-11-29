# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : yes_or_no
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2022/11/29 22:19
-------------------------------------------------
"""
from queue import Queue


def is_if_queue():
    q = Queue()
    q.put(1)
    q.put(2)

    if q.get():     # if 判断也会用掉一次，出一次队列
        pass

    print(q)        # 1 在 if 中用掉了，只剩下 2 了


if __name__ == "__main__":
    is_if_queue()
