# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 26
  Description :

------------ 用例 -------------
输入
<ABC<c89%000<
输出
ABc89%00,true

------------ 用例 -------------
输入
ABC<c89%000<
输出
ABc89%00,true

------------ 用例 -------------
输入
 ABC<c89%000<
输出
ABc89%00,true

------------ 用例 -------------
输入
ADSAas1235123
输出
ADSAas1235123,false

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/15 15:00
-------------------------------------------------
"""


def is_valid_password(password):
    """ 判断5个条件 """
    is_long = len(password) >= 8
    is_upper = any(i.isupper() for i in password)
    is_lower = any(i.islower() for i in password)
    is_digit = any(i.isdigit() for i in password)
    is_special = any(not (i.isalpha() or i.isdigit()) for i in password)        # **** 不全是数字和字母 ***

    return all([is_long, is_upper, is_lower, is_digit, is_special])         # all(    [    ]     )


def process_input(password):
    result = []
    for i in password:
        if i == "<" and result:
            result.pop()
        elif i == "<":
            continue
        else:
            result.append(i)

    return "".join(result)


if __name__ == "__main__":
    passward = input().strip()
    passward = process_input(passward)
    is_valid = "true" if is_valid_password(passward) else "false"
    print(f"{passward},{is_valid}")
