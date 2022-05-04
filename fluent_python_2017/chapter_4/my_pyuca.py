# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_pyuca
  Description : PyUCA 库（https://pypi.python.org/pypi/pyuca/），这是 Unicode 排序算法（Unicode Collation
                Algorithm，UCA）的纯 Python 实现

  Author      : chenyushencc@gmail.com
  date        : 2022/5/4 14:08
-------------------------------------------------
"""
import re
import unicodedata

import pyuca

if __name__ == '__main__':
    coll = pyuca.Collator()
    fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
    sorted_fruits = sorted(fruits, key=coll.sort_key)
    print(sorted_fruits)        # ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']

    re_digit = re.compile(r'\d')
    sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
    for char in sample:
        print('U+%04x' % ord(char),
              char.center(6),
              're_dig' if re_digit.match(char) else '-',
              'isdig' if char.isdigit() else '-',
              'isnum' if char.isnumeric() else '-',
              format(unicodedata.numeric(char), '5.2f'),
              unicodedata.name(char),
              sep='\t')

    """
    * 支持字符串和字节序列的双模式API
    """
    re_numbers_str = re.compile(r'\d+')
    re_words_str = re.compile(r'\w+')
    re_numbers_bytes = re.compile(rb'\d+')
    re_words_bytes = re.compile(rb'\w+')

    text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
                " as 1729 = 1³ + 12³ = 9³ + 10³.")
    text_bytes = text_str.encode('utf_8')
    """
    Text
      'Ramanujan saw ௧௭௨௯ as 1729 = 1³ + 12³ = 9³ + 10³.'
    Numbers
      str : ['௧௭௨௯', '1729', '1', '12', '9', '10']
      bytes: [b'1729', b'1', b'12', b'9', b'10']
    Words
      str : ['Ramanujan', 'saw', '௧௭௨௯', 'as', '1729', '1³', '12³', '9³', '10³']
      bytes: [b'Ramanujan', b'saw', b'as', b'1729', b'1', b'12', b'9', b'10']
    """
    print('Text', repr(text_str), sep='\n ')
    print('Numbers')
    print(' str :', re_numbers_str.findall(text_str))
    print(' bytes:', re_numbers_bytes.findall(text_bytes))
    print('Words')
    print(' str :', re_words_str.findall(text_str))
    print(' bytes:', re_words_bytes.findall(text_bytes))

