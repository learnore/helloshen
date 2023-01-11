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
from collections import OrderedDict
from queue import Queue


def is_if_queue():
    """ Queue 队列的 get() 会根据“先进先出”原则，弹出一个 """
    q = Queue()
    q.put(1)
    q.put(2)

    if q.get():     # if 判断也会用掉一次，出一次队列
        pass

    print(q)        # 1 在 if 中用掉了，只剩下 2 了


def queue_or_stack_ordereddict():
    """ 队列和栈(数组)对比 """
    q = Queue()     # 队列
    q.put(1)
    q.get()
    q.empty()
    q.full()

    l = []          # 栈(数组)
    l.append(1)
    l.pop(0)        # pop 移除索引位置 --"未加参数时直接移除数组的末尾元素"
    l.remove(1)     # remove 移除具体的值
    len(l)          # 判空

    o = OrderedDict()
    o[1] = 4        # 字典加入      OrderedDict([(1, 4)])
    o[2] = 5        # 字典加入      OrderedDict([(1, 4), (2, 5)])
    o[3] = 6        # 字典加入      OrderedDict([(1, 4), (2, 5), (3, 6)])
    o.pop(1)        # pop(key)     OrderedDict([(2, 5), (3, 6)])
    o.keys()        # 获取 o 的所有 key 值        odict_keys([2, 3])

    dict1 = {'a': 1}
    print(dict1.get('c', "happy new year~ dear"))       # happy new year~ dear  字典默认值 .get(key, 默认值)


def str_or_touple():
    print(("123",))     # ('123',)      元组
    print(("123"))      # 123           字符串


if __name__ == "__main__":
    q = Queue(maxsize=1)  # 队列
    q.put(1)
    print(q.full())
    q.get()
    q.put(2)
    print(q.full())
    q.get()
    print(q.empty())
    print(q.full())
