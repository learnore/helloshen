# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : registration
  Description : 1 装饰器的一个关键特性是，它们在被装饰的函数定义之后立即运行。这通常是在导入时（即 Python 加载模块时）
                2 函数装饰器在导入模块时立即执行，而被装饰的函数只在明确调用时运行。这突出了 Python 程序员所说的导入时和运行时之间的区别。

                > > > import registration
                running register(<function f1 at 0x10063b1e0>)
                running register(<function f2 at 0x10063b268>)

                 > > > registration.registry
                [<function f1 at 0x10063b1e0>, <function f2 at 0x10063b268>]

                • 装饰器函数与被装饰的函数在同一个模块中定义。实际情况是，装饰器通常在一个模块中定义，然后应用到其他模块中的函数上。
                • register 装饰器返回的函数与通过参数传入的相同。实际上，大多数装饰器会在内部定义一个函数，然后将其返回。

  Author      : chenyushencc@gmail.com
  date        : 2022/5/29 11:31
-------------------------------------------------
"""
registry = []       # registry 保存被 @register 装饰的函数引用。


def register(func):     # register 的参数是一个函数。
    print("running register (%s)" % func)       # 为了演示，显示被装饰的函数。
    registry.append(func)
    return func


@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


def f3():
    print("running f3()")


def main():
    print("running main()")
    print("registry -> ", registry)     # main 显示 registry，然后调用 f1()、f2() 和 f3()
    f1()
    f2()
    f3()


if __name__ == "__main__":
    """
    Console Output --> 
    
    running register (<function f1 at 0x000002758CCE4310>)
    running register (<function f2 at 0x000002758CCE4A60>)
    running main()
    registry ->  [<function f1 at 0x000002758CCE4310>, <function f2 at 0x000002758CCE4A60>]
    running f1()
    running f2()
    running f3()
    """
    main()
