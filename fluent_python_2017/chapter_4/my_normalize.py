# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_normalize
  Description : 规范化字符
  Author      : chenyushencc@gmail.com
  date        : 2022/5/4 13:41
-------------------------------------------------
"""
import locale

from unicodedata import normalize

if __name__ == '__main__':
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1, s2)
    print(len(s1), len(s2))         # 4 5 码位不一样
    print(s1 == s2)
    print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))     # NFC（Normalization Form C）使用最少的码位构成等价的字符串
    print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))     # NFD 把组合字符分解成基字符和单独的组合字符
    print(normalize('NFC', s1) == normalize('NFC', s2))
    print(normalize('NFD', s1) == normalize('NFD', s2))

    """
    * 在 Python 中，非 ASCII 文本的标准排序方式是使用 locale.strxfrm 函数，根据 locale 模
    * 块的文档（https://docs.python.org/3/library/locale.html?highlight=strxfrm#locale.strxfrm），这
    * 个函数会“把字符串转换成适合所在区域进行比较的形式”
    * 
    * 使用 locale.strxfrm 函数之前，必须先为应用设定合适的区域设置，还要祈祷操作系统支持这项设置。
    * 在区域设为 pt_BR 的 GNU/Linux（Ubuntu 14.04）中，可以使用示例 4-19 中的命令
    """
    # print(locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8'))
    fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
    print(sorted(fruits))                                   # ['acerola', 'atemoia', 'açaí', 'caju', 'cajá']
    locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
    print(sorted(fruits, key=locale.strxfrm))               # ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']


