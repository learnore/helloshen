# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_setcomps
  Description : 集合推导
  Author      : chenyushencc@gmail.com
  date        : 2022/5/2 23:42
-------------------------------------------------
"""
from unicodedata import name


if __name__ == '__main__':
    """
    * 新建一个 Latin-1 字符集合，该集合里的每个字符的 Unicode 名字里都有“SIGN”这个单词
    """
    print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})
