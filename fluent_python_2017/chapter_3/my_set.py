# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_set
  Description : “集”或者“集合”既指 set，也指 frozenset
  Author      : chenyushencc@gmail.com
  date        : 2022/5/2 23:19
-------------------------------------------------
"""


if __name__ == '__main__':
    l = ['spam', 'spam', 'eggs', 'spam']
    print(set(l))       # 集合的本质是许多唯一对象的聚集。因此，集合可以用于去重
    print(list(set(l)))

    """
    * 除了保证唯一性，集合还实现了很多基础的中缀运算符 。给定两个集合 a 和 b
    * set(a) | set(b) 返回的是它们的合集
    * set(a) & set(b) 得到的是交集
    * set(a) - set(b) 得到的是差集
    """

    """
    found = len(needles & haystack)
    
    等同于
    
    found = 0
    for n in needles:
        if n in haystack:
            found += 1
    """
    needles = set('aeaarfg')
    haystack = set('efdghjhhgfds')
    common_set = needles & haystack     # 交集，多个只取一个哦
    print(common_set)                   # {'g', 'e', 'f'}
    found = len(common_set)
    print(found)                        # 3 == print(len(needles & haystack))

    """
    * 改为 可以用在任何可迭代对象上
    """
    print(len(set(needles) & set(haystack)))
    print(len(set(needles).intersection(haystack)))     # 这种写法会牵扯到把对象转化为集合的成本

    """
    * 句法的陷阱：{} 是 空字典，不是空集，空集是 set()
    """
