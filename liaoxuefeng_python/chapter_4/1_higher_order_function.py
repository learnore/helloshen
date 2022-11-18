# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 1_higher_order_function
  Description : 高阶函数
                函数名也是变量: 函数本身也可以赋值给变量，即：变量可以指向函数

  Author      : chenyushencc@gmail.com
  date        : 2022/11/17 21:43
-------------------------------------------------
"""
from functools import reduce

if __name__ == "__main__":
    """ 函数名是指向函数的变量，所以高阶函数，就是将一个函数接收另一个函数作为参数 """
    def add(x, y, f):
        return f(x) + f(y)

    print(add(-5, 6, abs))      # 11
    """ 函数式编程就是指这种高度抽象的编程范式 """

    # ---------------------------------------------------------------------------
    """ map """
    """
    # map()函数接收两个参数，一个是函数，一个是 Iterable
    # map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
    """
    def my_func1(x):
        return x * x

    res1 = map(my_func1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(res1)           # <map object at 0x0000021CC3572D40>
    print(list(res1))     # [1, 4, 9, 16, 25, 36, 49, 64, 81]

    """ 把这个list所有数字转为字符串 """
    print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))      # ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # ---------------------------------------------------------------------------
    """ reduce
    # reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
    # reduce把结果继续和序列的下一个元素做累积计算，其效果就是
    #   reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
    """
    def my_func2(x, y):
        return x * 10 + y

    print(reduce(my_func2, [1, 3, 5, 7, 9]))     # 13579


    def my_func3(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    test1 = list(map(my_func3, "13579"))
    print(test1)     # [1, 3, 5, 7, 9]       字符串相当于一个 Iterable
    print(reduce(my_func2, test1))          # 13579

    """ 用lambda函数进一步简化 """
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def char2num(s):
        return DIGITS[s]

    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num, s))
    print(str2int("13579"))     # 13579

    # ---------------------------------------------------------------------------
    """ filter 用于过滤序列，把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。 """
    def is_odd(n):
        return n % 2 == 1

    print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))     # [1, 5, 9, 15]

    """ 用filter求素数 """
    def _odd_iter():        # 无限序列
        n = 1
        while True:
            n += 2
            yield n

    o = _odd_iter()
    print(next(o))      # 3
    print(next(o))      # 5
    print(next(o))      # 7

    def _not_divisible(n):
        return lambda x: x % n > 0

    def primes():
        yield 2
        it = _odd_iter()        # 初始化序列
        while True:
            n = next(it)
            yield n
            it = filter(_not_divisible(n), it)      # 构造新的序列

    print(primes())         # <generator object primes at 0x0000028308E69F50>
    p = primes()
    print(next(p))   # 2
    print(next(p))   # 3
    print(next(p))   # 5
    print(next(p))   # 7
    print("----------------")
    """
    2
    3
    5
    7
    """
    for n in primes():
        if n < 10:      # 只筛选出 10 以内的素数
            print(n)
        else:
            break

    # ---------------------------------------------------------------------------
    """ sorted """
    print(sorted([36, 5, -12, 9, -21]))     # [-21, -12, 5, 9, 36]
    print(sorted([36, 5, -12, 9, -21], key=abs))        # [5, 9, -12, -21, 36]
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.upper))     # ['about', 'bob', 'Credit', 'Zoo']
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.upper, reverse=True))     # ['Zoo', 'Credit', 'bob', 'about']

    # ---------------------------------------------------------------------------
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    def by_name(stu):
        return stu[0]

    def by_score(stu):
        return stu[1]

    print(sorted(L, key=by_name))  # [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
    print(sorted(L, key=by_score))  # [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]

