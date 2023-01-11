# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 4_decorator
  Description : - 装饰器：拓展原来函数功能的一种函数
                - decorator 必须是一个“可被调用（callable）的对象     __call__
                - 在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
                - 装饰器，decorator就是一个返回函数的高阶函数


  Author      : chenyushencc@gmail.com
  date        : 2022/11/18 17:09
-------------------------------------------------
"""
import functools

if __name__ == "__main__":
    def log1(func):
        def wrapper(*args, **kw):
            print("call %s(): " % func.__name__)
            return func(*args, **kw)
        return wrapper

    @log1        # 相当于 now1 = log1(now1)
    def now1():
        print("2022/11/18 17:09")

    """
    # call now1(): 
    # 2022/11/18 17:09
    """
    now1()

    def log2(text):
        def decorator(func):
            def wrapper(*args, **kw):
                print("%s %s():" % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator

    @log2("execute")        # now2 = log2('execute')(now2)
    def now2():
        print("2022/11/18 17:09")

    """
    # execute now2():
    # 2022/11/18 17:09
    """
    now2()

    print(now1.__name__)        # wrapper
    print(now2.__name__)        # wrapper

    # ---------------------------------------------------------------------------
    def log3(func):
        @functools.wraps(func)      # 需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
        def wrapper(*args, **kw):
            print("call %s(): " % func.__name__)
            return func(*args, **kw)
        return wrapper


    @log3
    def now3():
        print("2022/11/18 17:09")

    print(now3.__name__)        # now3