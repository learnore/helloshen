# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 4_decorator
  Description : 装饰器，decorator就是一个返回函数的高阶函数

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

    @log1        # 相当于 now = log(now)
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

    @log2("execute")        # now = log('execute')(now)
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