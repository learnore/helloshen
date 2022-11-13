#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : ASCII_Unicode_UTF-8
  Description : https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896
  Author      : chenyushencc@gmail.com
  date        : 2022/11/2 20:39
-------------------------------------------------
"""

if __name__ == "__main__":
    """
    # ASCII     ASCII编码是1个字节
    # Unicode   Unicode编码通常是2个字节（现代操作系统和大多数编程语言都直接支持Unicode）
    # UTF-8     UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，
    #           常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节
    """
    print(ord('A'))     # 65
    print(chr(65))      # A
    print(ord('中'))            # 20013
    print('\u4e2d\u6587')       # 中文            0x4e2d = 20013

    """ 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes """
    print('ABC'.encode('ascii'))    # b'ABC'        （纯英文的str可以用ASCII编码为bytes，内容是一样的）
    print('中文'.encode('utf-8'))    # b'\xe4\xb8\xad\xe6\x96\x87'
    """
    # Traceback  - UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
    # 含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错
    """
    # print('中文'.encode('ascii'))

    """ 我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes ,要把bytes变为str，就需要用decode()方法 """
    print(b'ABC'.decode('ascii'))       # ABC
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))      # 中文

    """ 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节 """
    print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

    """
    # 占位符号
    # %d    整数
    # %f	浮点数
    # %s	字符串
    # %x	十六进制整数
    # 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
    """
    print('Age: %s. Gender: %s' % (25, True))       # Age: 25. Gender: True
    print('growth rate: %d %%' % 7)     # growth rate: 7 %          (用%%来表示一个%)
    print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))        # Hello, 小明, 成绩提升了 17.1%

    r = 2.5
    s = 3.14 * r ** 2
    print(f'The area of a circle with radius {r} is {s:.2f}')       # The area of a circle with radius 2.5 is 19.62
