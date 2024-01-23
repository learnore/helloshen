# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 60
  Description :

🎃样例1
输入
9
输出
9=9
9=4+5
9=2+3+4
Result:3
说明：
整数9有三种表示方法，第1个表达式只有1个自然数,最先输出,
第2个表达式有2个自然数，第2次序输出,
第3个表达式有3个自然数，最后输出。
每个表达式中的自然数都是按递增次序输出的。
数字与符号之间无空格


🎃样例2
输入
10
输出
10=10
10=1+2+3+4
Result:2

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/20 10:38
-------------------------------------------------
"""


def solution(n):
    """
    解题思路：
    1、必有1个答案是：自己=自己
    2、超过自己的一半时，就可以不用查找了，比如：5+6 = 11 > 9了
    3、注意题目2点特殊要求
    """
    count = 1
    results = [f"{n}={n}"]

    for i in range(n//2, 0, -1):
        cur_str = f"{i}"
        cur_result = i

        while cur_result < n:
            i += 1
            cur_result += i
            cur_str += f"+{i}"

        if cur_result == n:
            results.append(f"{n}=" + cur_str)
            count += 1

    return results, count


if __name__ == "__main__":
    n = int(input().strip())
    results, count = solution(n)
    for i in results:
        print(i)

    print(f"Result:{count}")
