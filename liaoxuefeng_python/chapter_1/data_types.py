# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : data_types
  Description : Python 基础 - 数据类型 & 变量
  Author      : chenyushencc@gmail.com
  date        : 2022/11/1 22:10
-------------------------------------------------
"""

if __name__ == "__main__":
    """ --- 数字为了便于读，可用 _ 连接数字(但是不可以在首位使用 _ ， 比如 _100_0000 是会报错的) --- """
    # 整数
    million = 1_00_0000       # <class 'int'> 1000000
    hex_num = 0x_1_1          # <class 'int'> 17
    print(type(million))
    print(type(hex_num))

    # 浮点数:  Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）
    float_num1 = 1.23e5        # <class 'float'> 123000.0
    float_num2 = 1.23e-5       # <class 'float'> 1.23e-05
    float_num2_res = float_num2 * 100_000       # <class 'float'>  1.23
    print(type(float_num1))
    print(type(float_num2))
    print(type(float_num2_res))

    """ --- 整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。 --- """

    # 字符串
    str_demo1 = "I'm OK"        # <class 'str'>
    str_demo2 = 'I\'m \"OK\"!'
    print('\\\t\\')     # \	\
    print(r'\\\t\\')    # \\\t\\        r'' 表示''内部的字符串默认不转义
    str_block = '''line1        
line2
line3'''
    print(str_block)       # '''...'''的格式表示多行内容
    print(r'''hello,\n
    world''')

    # 布尔值
    x1 = 100 or 200     # or 时 首先遇到的 True 就直接返回了
    x2 = 200 or 100
    y0 = 0 and 100      # and 时 首先遇到的 False 就直接返回，否则就继续找后面的
    y1 = 100 and 200
    y2 = 200 and 100
    print(x1, x2)       # 100 200
    print(y0, y1, y2)   # 0 200 100

    # 空值: None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
    None

    # 变量: 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
    a = 'ABC'
    b = a
    a = 'XYZ'
    print(b)        # ABC

    # 常量: 通常用全部大写的变量名表示常量
    PI = 3.14159265359      # 用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你

    # ------------
    print(10 / 3)       # 3.3333333333333335    /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
    print(9 / 3)        # 3.0       /除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数
    print(9 // 3)       # 3         还有一种除法是//，称为地板除，两个整数的除法仍然是整数
    print(10 % 3)       # 1         取余
