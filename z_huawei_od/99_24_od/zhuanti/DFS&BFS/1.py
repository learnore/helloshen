# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 1
  Description : 解密犯罪时间(DFS)

🎃题目描述
警察在侦破一个案件时，得到了线人给出的可能犯罪时间，形如 “HH:MM” 表示的时刻。

根据警察和线人的约定，为了隐蔽，该时间是修改过的，

解密规则为：利用当前出现过的数字，构造下一个距离当前时间最近的时刻，则该时间为可能的犯罪时间。

每个出现数字都可以被无限次使用。

🎃输入输出
输入
形如HH:SS字符串，表示原始输入。

输出
形如HH:SS的字符串，表示推理处理的犯罪时间

备注

1、可以保证现任给定的字符串一定是合法的。

例如，“01:35”和“11:08”是合法的，“1:35”和“11:8”是不合法的。

2、最近的时刻可能在第二天

🎃样例1
20:12得到20:20
23:59得到22:22
12:58得到15:11
18:52得到18:55
23:52得到23:53
09:17得到09:19
07:08得到08:00


  Summary     : 1、也谈不上DFS吧
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/21 12:42
-------------------------------------------------
"""


def decrypt_time(input_time):
    """
    解题思路：
    1、从当前时间点，换算成分钟总数，依次+1分钟
    2、将新的时间总数换回 hh:mm ，判断这4个字符是否在原来的几个时间字符中
    3、关键的语法糖：
            set()
            set.add()
            (current_time_in_minutes+1) % (24 * 60)
            divmod(next_time_in_minutes, 60)
            str.rjust(2, '0')

    """
    # 构造集合
    set_res = set()
    for c in input_time:
        if ord("0") <= ord(c) <= ord("9"):
            set_res.add(c)

    # 将时间转换成分钟表示
    hour, minute = map(int, input_time.split(':'))
    current_time_in_minutes = hour * 60 + minute

    while True:
        current_time_in_minutes += 1
        # 构造下一个距离当前时间最近的时刻
        next_time_in_minutes = current_time_in_minutes % (24 * 60)
        # 将下一个时刻转换成小时和分钟表示
        next_hour, next_minute = divmod(next_time_in_minutes, 60)
        # str_hours = f"{next_hour:02d}{next_minute:02d}"     # 补充2位
        str_hours = str(next_hour).rjust(2, "0") + str(next_minute).rjust(2, "0")

        is_pass = [False, False, False, False]
        for i in range(len(str_hours)):
            if str_hours[i] in set_res:
                is_pass[i] = True
            else:
                break
        if all(is_pass):
            return str(next_hour).rjust(2, "0") + ":" + str(next_minute).rjust(2, "0")


if __name__ == "__main__":
    # 样例测试
    print(decrypt_time("20:12"))  # 输出 20:20
    print(decrypt_time("23:59"))  # 输出 22:22
    print(decrypt_time("12:58"))  # 输出 15:11
    print(decrypt_time("18:52"))  # 输出 18:55
    print(decrypt_time("23:52"))  # 输出 23:53
    print(decrypt_time("09:17"))  # 输出 09:19
    print(decrypt_time("07:08"))  # 输出 08:00
