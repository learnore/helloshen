# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 39
  Description :

--- 用例1
输入
4
cat
bt
hat
tree
atach??
输出
3


--- 用例2
输入
4
cat
bt
hat
tree
atarh??
输出
4




  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/17 21:55
-------------------------------------------------
"""
import copy


def solution(n, words, chars):
    """ 循环 words 单词，从 chars 中找字母，每次拼写单词时？只能用1次 """
    results = 0
    chars = [i for i in chars]

    for w in words:
        temp_chars = copy.deepcopy(chars)
        is_read = True
        for i in w:
            if i in temp_chars:
                temp_chars.remove(i)        # 1个字母只能用一次
            elif i not in temp_chars and "?" in temp_chars:
                temp_chars.remove("?")      # 移除第一个 ?
            else:
                is_read = False
                break

        if is_read:
            results += 1

    return results


if __name__ == "__main__":
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    chars = input().strip()

    results = solution(n, words, chars)
    print(results)
