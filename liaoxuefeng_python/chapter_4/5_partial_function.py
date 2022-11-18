# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 5_partial_function
  Description : 偏函数（Partial function）
  Author      : chenyushencc@gmail.com
  date        : 2022/11/18 17:29
-------------------------------------------------
"""
import functools

if __name__ == "__main__":
    """ int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换 """
    print(int('12345'))     # 12345
    print(int('12345', 16))     # 74565         将 12345 作为 16 进制转为 10 进制

    def int2(x, base=2):
        return int(x, base)
    print(int2("10101111"))     # 175

    """ functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2 """
    int2 = functools.partial(int, base=2)
    """ 相当于 """
    kw = {"base": 2}
    print(int("10101111", **kw))        # 175

    # -----------------------------------------------------------------------
    max2 = functools.partial(max, 10)
    print(max2(5, 6, 7))        # 10
    """ 相当于 """
    args = (10, 5, 6, 7)
    print(max(*args))           # 10
    