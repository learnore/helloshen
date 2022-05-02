# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_setdefault
  Description : 用setdefault处理找不到的键

                my_dict.setdefault(key, []).append(new_value)

                等同于

                if key not in my_dict:
                    my_dict[key] = []
                my_dict[key].append(new_value)

  Author      : chenyushencc@gmail.com
  date        : 2022/5/2 20:00
-------------------------------------------------
"""
import re
import sys

if __name__ == '__main__':
    WORD_RE = re.compile(r'\w+')

    index = {}
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            word = re.match.group()
            column_no = re.match.start() + 1
            location = (line_no, column_no)

            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences

    for word in sorted(index, key=str.upper()):
        print(word, index[word])

    # --------------------------- 等同于 ------------------------------------------

    WORD_RE = re.compile(r'\w+')

    index = {}
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                index.setdefault(word, []).append(location)     # index.setdefault(word, []) == index[word] 然后赋值，很保险

    for word in sorted(index, key=str.upper()):
        print(word, index[word])
