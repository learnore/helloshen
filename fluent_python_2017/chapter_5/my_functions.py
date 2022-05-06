# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_functions
  Description : 函数的 __doc__ 属性
  Author      : chenyushencc@gmail.com
  date        : 2022/5/4 22:16
-------------------------------------------------
"""
from functools import reduce            # 从 Python 3.0 起，reduce 不再是内置函数了
from operator import add                # 导入 add，以免创建一个专求两数之和的函数


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n-1)


def reverse(word):
    return word[::-1]


if __name__ == '__main__':
    # ----------------------------- 一等函数 -------------------------------------------
    print(factorial(42))            # 在运行时创建
    print(factorial.__doc__)        # __doc__ 属性用于生成对象的帮助文本
    print(type(factorial))

    fact = factorial                # 通过别的名称使用函数，再把函数作为参数传递
    print(fact)                     # <function factorial at 0x...>
    print(fact(5))                  # 120
    """
    * map 函数返回一个可迭代对象，里面的元素是把第一个参数（一个函数）应用到第二个参数（一个可迭代对象
    * 这里是 range(11)）中各个元素上得到的结果
    """
    print(map(factorial, range(6)))         # <map object at 0x...>    把它作为参数传给 map 函数
    print(list(map(factorial, range(6))))   # [1, 1, 2, 6, 24, 120]

    # ----------------------------- 高阶函数 map、filter、reduce -------------------------------------------

    """
    * 接受函数为参数，或者把函数作为结果返回的函数是高阶函数（higher-order function）
    """
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=len))      # ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']   若想根据单词的长度排序，只需把 len 函数传给 key 参数
    print(reverse('testing'))           # gnitset
    print(sorted(fruits, key=reverse))      # ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']

    """
    * 计算阶乘列表：map 和 filter 与列表推导比较
    """
    print(list(map(fact, range(6))))
    print([fact(i) for i in range(6)])
    print(list(map(fact, filter(lambda n: n % 2, range(6)))))
    print([fact(n) for n in range(6) if n % 2])

    """
    * 使用 reduce 和 sum 计算 0~99 之和
    """
    print(reduce(add, range(100)))
    print(sum(range(100)))          # 使用 sum 做相同的求和；无需导入或创建求和函数

    """
    * all 和 any 也是内置的归约函数。
    * all(iterable)
    *     如果 iterable 的每个元素都是真值，返回 True；all([]) 返回 True。
    * any(iterable)
    *     只要 iterable 中有元素是真值，就返回 True；any([]) 返回 False。
    """
    print(all([]))
    print(any([]))

    """
    * 函数内省  dir(function)
    * ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', 
    * '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', 
    * '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', 
    * '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', 
    * '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    """
    print(dir(factorial))

    """
    * 计算差集，然后排序，得到类的实例没有而函数有的属性列表
    """
    class C: pass
    obj = C()
    def func(): pass
    """
    * ['__annotations__', '__builtins__', '__call__', '__closure__', '__code__', '__defaults__', 
    * '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
    """
    print(sorted(set(dir(func)) - set(dir(obj))))
