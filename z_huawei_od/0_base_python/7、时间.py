# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 7、时间
  Description : T34
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/17 15:55
-------------------------------------------------
"""
from datetime import datetime


def compare_times(time_str1, time_str2):
    """ 将 hh:mm 转换成分钟，便于比较大小 """
    time1, time2 = hhmm_mm(time_str1), hhmm_mm(time_str2)

    # 将时间字符串解析为时间对象
    # time1 = datetime.strptime(time_str1, "%H:%M")
    # time2 = datetime.strptime(time_str2, "%H:%M")

    # 比较两个时间对象
    if time1 < time2:
        return f"{time_str1} 小于 {time_str2}"
    elif time1 > time2:
        return f"{time_str1} 大于 {time_str2}"
    else:
        return f"{time_str1} 等于 {time_str2}"


def hhmm_mm(hhmm):
    """ 将时间 hh:mm 变成分钟 """
    h, m = map(int, hhmm.split(":"))
    return h*60 + m


def is_overlap(start_time_i, end_time_i, start_time_j, end_time_j):
    """ 判断2个时间段是否重叠（重叠情况比较复杂，直接考虑未重叠情况） """
    # 将 hh:mm 转成分钟，方便比较
    start_time_i = hhmm_mm(start_time_i)
    end_time_i = hhmm_mm(end_time_i)
    start_time_j = hhmm_mm(start_time_j)
    end_time_j = hhmm_mm(end_time_j)

    # 逻辑
    if end_time_i < start_time_j or end_time_j < start_time_i:
        return f"没重叠"
    else:
        return f"重叠了"


if __name__ == "__main__":
    print(compare_times("7:11", "6:12"))
    print(is_overlap("6:10", "7:00", "6:30", "7:30"))
