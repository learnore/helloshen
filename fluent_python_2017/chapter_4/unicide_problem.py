# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : unicide_problem
  Description : 字符问题
                把 码位 转换成 字节序列 的过程是 编码
                把 字节序列 转换成 码位 的过程是 解码

                如果想帮助自己记住 .decode() 和 .encode() 的区别，可以把字节序列想成
                晦涩难懂的机器磁芯转储，把 Unicode 字符串想成“人类可读”的文本。那
                么，把字节序列变成人类可读的文本字符串就是解码，而把字符串变成用于
                存储或传输的字节序列就是编码。

  Author      : chenyushencc@gmail.com
  date        : 2022/5/3 10:41
-------------------------------------------------
"""


if __name__ == '__main__':
    s = 'café'
    print(len(s))
    b = s.encode('utf8')                # 编码
    print(b)
    print(len(b))
    print(b.decode('utf8'))             # 解码

    cafe = bytes('café', encoding='utf-8')
    print(cafe)
    print(cafe[0])                      # 各个元素是 range(256) 内的整数
    print(cafe[:1])                     # bytes 对象的切片还是 bytes 对象，即使是只有一个字节的切片
    cafe_arr = bytearray(cafe)
    print(cafe_arr)
    print(cafe_arr[-1:])

    print(bytes.fromhex('31 4A CE A9'))     # 解析十六进制数字对（数字对之间的空格是可选的），构建二进制序列
