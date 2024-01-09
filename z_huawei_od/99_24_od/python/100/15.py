# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 15
  Description :
  Summary     : 1、对输入字符进行空格处理
                    str.strip()                 # 去除字符串的前后空格
                    str.replace(" ", "")        # 去除字符串内所有的空格
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/9 10:09
-------------------------------------------------
"""


def sort_flights(flights):
    # flights.sort(lambda x: (x[:2], int(x[2:])), reverse=False)
    sorted_flights = sorted(flights, key=lambda x: (x[:2], int(x[2:])))
    return sorted_flights


if __name__ == "__main__":

    input_flights = input().strip().split(",")
    # 对输入的航班信息进行去除两端的空白字符处理
    input_flights = [flight.replace(" ", "").strip() for flight in input_flights]

    # 调用排序函数获取排序后的航班信息
    results = sort_flights(input_flights)
    print(",".join(results))
