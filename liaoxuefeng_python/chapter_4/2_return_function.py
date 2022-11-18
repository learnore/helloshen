# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 2_return_function
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2022/11/18 16:00
-------------------------------------------------
"""

if __name__ == "__main__":
    """
    # 我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
    # 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力
    """
    def lazy_sum(*args):
        def sum():
            res = 0
            for n in args:
                res += n

            return res

        return sum

    f1 = lazy_sum(1, 3, 5, 7, 9)
    f2 = lazy_sum(1, 3, 5, 7, 9)
    print(f1)       # <function lazy_sum.<locals>.sum at 0x000001F5C936FBE0>
    print(f1())     # 25
    print(f1 == f2)     # False     f1()和f2()的调用结果互不影响

    # --------------------------------------------------
    def count1():
        res = []
        for i in range(1, 4):
            def f():
                return i*i
            res.append(f)

        return res

    c1, c2, c3 = count1()        # [9, 9, 9]
    """ 
    # [<function count.<locals>.f at 0x000001337B972B00>,
    #  <function count.<locals>.f at 0x000001337B972B90>,
    #  <function count.<locals>.f at 0x000001337B972C20>]
    # 可以看作是返回的函数的引用，最后引用的都是最后的值 9
    # 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
    """
    print(c1())     # 9
    print(c2())     # 9
    print(c3())     # 9

    def count2():
        def f(i):
            return i * i

        res = []
        for i in range(1, 4):
            res.append(f(i))

        return res

    c4, c5, c6 = count2()
    print(c4, c5, c6)       # 1 4 9

    # --------------------------------------------------
    def inc():
        x = 0
        def fn():
            """ 需要先使用nonlocal声明该变量不是当前函数的局部变量 """
            nonlocal x      # Python解释器会把x当作函数fn()的局部变量，它会报错，必须使用 nonlocal 关键字声明
            x = x + 1
            return x
        return fn

    i = inc()
    print(i())      # 1
    print(i())      # 2

    # --------------------------------------------------
    """ 利用闭包返回一个计数器函数，每次调用它返回递增整数 """
    def createCounter():
        x = 0
        def counter():
            nonlocal x
            x += 1
            return x

        return counter


    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())       # 1 2 3 4 5



