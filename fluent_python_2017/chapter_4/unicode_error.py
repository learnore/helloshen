# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : unicode_error
  Description : UnicodeEncodeError（把字符串转换成二进制序列时） 编码错误
                UnicodeDecodeError（把二进制序列转换成字符串时） 解码错误

                关于编码默认值的最佳建议是：别依赖默认值

  Author      : chenyushencc@gmail.com
  date        : 2022/5/4 11:11
-------------------------------------------------
"""


if __name__ == '__main__':
    """
    编码错误    UnicodeEncodeError
    """
    city = 'São Paulo'
    # print(city.encode('cp437'))     # UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>
    print(city.encode('cp437', errors='ignore'))        # b'So Paulo'
    print(city.encode('cp437', errors='replace'))       # b'S?o Paulo'
    print(city.encode('cp437', errors='xmlcharrefreplace'))     # b'S&#227;o Paulo'     'xmlcharrefreplace' 把无法编码的字符替换成 XML 实体

    """
    解码错误    UnicodeDecodeError
    乱码字符称为鬼符（gremlin）或 mojibake（文字化け，“变形文本”的日文）
    """
    octets = b'Montr\xe9al'
    print(octets.decode('cp1252'))
    """
    * UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte
    """
    # print(octets.decode('utf-8'))
    """
    * 使用 'replace' 错误处理方式，\xe9 替换成了“�”（码位是 U+FFFD），这是官方指定的 REPLACEMENT CHARACTER（替换字符），表示未知字符
    """
    print(octets.decode('utf-8', errors='replace'))     # Montr�al



