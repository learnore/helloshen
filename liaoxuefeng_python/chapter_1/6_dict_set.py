# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : dict_set
  Description : https://www.liaoxuefeng.com/wiki/1016959663602400/1017104324028448
  Author      : chenyushencc@gmail.com
  date        : 2022/11/2 22:26
-------------------------------------------------
"""

if __name__ == "__main__":
    """ 判断 dict 的 KeyError """
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print('Thomas' in d)        # False
    print(d.get('Thomas'))      # None      get 没有值就是 None
    print(d.get('Thomas', -1))  # -1        get 自定义值
    d.pop('Bob')                # {'Michael': 95, 'Tracy': 85}
    print(d)

    """ set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。 """
    """ 要创建一个set，需要提供一个list作为输入集合 """
    s = set([1, 2, 3])
    print(s)        # {1, 2, 3}
    """ 重复元素在set中自动被过滤 """
    s = set([1, 1, 2, 2, 3, 3])
    print(s)        # {1, 2, 3}
    """ 通过add(key)方法可以添加元素到set中 """
    s.add(4)
    print(s)        # {1, 2, 3, 4}
    """ 通过remove(key)方法可以删除元素 """
    s.remove(4)
    print(s)        # {1, 2, 3}
    """ set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作 """
    s1 = set([1, 2, 3])
    s2 = set([2, 3, 4])
    print(s1 & s2)      # {2, 3}
    print(s1 | s2)      # {1, 2, 3, 4}

    s3 = set([1, 2, 3])
    s4 = set([1, 2, 3])
    print(s3 == s4)         # True



