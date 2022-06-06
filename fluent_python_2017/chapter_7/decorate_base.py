# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : decorate_base
  Description : 装饰器是可调用的对象，其参数是另一个函数（被装饰的函数）。装饰器可能会处理被装
                饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象。
  Author      : chenyushencc@gmail.com
  date        : 2022/5/29 10:50
-------------------------------------------------
"""


def deco(func):
    def inner():
        print("running inner()")

    return inner        # deco 返回 inner 函数对象


@deco
def target():       # 使用 deco 装饰 target
    print("running target()")


def no_deco_target():
    print("running target()")


if __name__ == "__main__":
    """ Console Output --> running inner() """
    target()        # 调用被装饰的 target 其实会运行 inner
    """ Console Output --> running target() """
    no_deco_target()

    """ Console Output --> <function deco.<locals>.inner at 0x0000022BE1B84A60> """
    """ *** 装饰器的一大特性是，能把被装饰的函数替换成其他函数。 """
    print(target)   # 审查对象，发现 target 现在是 inner 的引用。
    """ Console Output --> <function no_deco_target at 0x0000022BE1B84310> """
    print(no_deco_target)

