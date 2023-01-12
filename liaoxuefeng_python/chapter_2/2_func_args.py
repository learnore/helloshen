# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 2_func_args
  Description : 函数的参数
                为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，
                这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
                同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

                Python中定义函数，参数定义的顺序必须是：
                    位置参数
                    默认参数
                    可变参数
                    关键字参数

                小结：
                1、
                *args 是 可变参数；
                    可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))
                **kw 是 关键字参数：
                    关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})

                2、*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法
                3、定义命名的 关键字参数 在没有 可变参数 的情况下不要忘了写分隔符*，否则定义的将是 位置参数


  Author      : chenyushencc@gmail.com
  date        : 2022/11/13 11:08
-------------------------------------------------
"""


def add_end1(L=[]):         # 定义默认参数要牢记一点：默认参数必须指向不变对象！
    L.append('END')
    return L


def add_end2(L=None):       # 定义默认参数要牢记一点：默认参数必须指向不变对象！
    if L is None:
        L = []

    L.append('END')
    return L


def calc(*numbers):         # 可变参数：* 可以传入任意个参数，包括0个参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def person1(name, age, **kw):        # 关键字参数 kw
    return ('name:', name, 'age:', age, 'other:', kw)


def person2(name, age, *, city, job):
    """ 要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数 """
    return (name, age, city, job)


def person3(name, age, *, city='Beijing', job):
    """ 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了 """
    """ 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数 """
    return (name, age, city, job)


def person4(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass


if __name__ == "__main__":
    print(add_end1())       # ['END', 'END' ...]        随着调用次数增多，里面的 END 也会越来越多
    print(add_end2())       # ['END']                   永远只有一个 END

    print(calc(1, 2))       # 5
    print(calc())           # 0
    nums = [1, 2, 3]
    print(calc(*nums))      # 14         Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去

    print(person1('Adam', 45, gender='M', job='Engineer'))   # ('name:', 'Adam', 'age:', 45, 'other:', {'gender': 'M', 'job': 'Engineer'})
    """
    # **extra 表示把 extra 这个 dict 的所有 key-value 用关键字参数传入到函数的 **kw 参数，kw 将获得一个 dict
    # 注意 kw 获得的 dict 是 extra 的一份拷贝，对 kw 的改动不会影响到函数外的 extra
    """
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    print(person1('Jack', 24, **extra))          # ('name:', 'Jack', 'age:', 24, 'other:', {'city': 'Beijing', 'job': 'Engineer'})
    print(person2('Jack', 24, city='Beijing', job='Engineer'))      # ('Jack', 24, 'Beijing', 'Engineer')
    print(person3('Jack', 24, job='Engineer'))      # ('Jack', 24, 'Beijing', 'Engineer')




