# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 54
  Description :

🎃样例1
输入
3 2
yuwen shuxue
fangfang 95 90
xiaohua 88 98
minmin 100 82
shuxue
输出
xiaohua fangfang minmin


🎃样例2
输入
3 2
yuwen shuxue
fangfang 95 90
xiaohua 88 95
minmin 90 95
zongfen
输出
fangfang minmin xiaohua
说明:
排序科目不存在，按总分排序，fangfang 和 minmin总分相同，按姓名的字典序顺序，fangfang 排在前面

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/19 13:21
-------------------------------------------------
"""


def solution(projects, students, kemu):
    """
    根据 kemu 从大到小输出学生名称，没有科目就按总分从大到小输出人名
    """
    results = []
    index = -1
    if kemu in projects:
        index = projects.index(kemu)

        students.sort(key=lambda x:x[index+1], reverse=True)
        for s in students:
            results.append(s[0])

    else:       # 没有找到科目就按照总分从大到小排序
        for s in students:
            sum_s = sum([int(i) for i in s[1:]])
            s.append(sum_s)

        students.sort(key=lambda x: x[-1], reverse=True)
        for s in students:
            results.append(s[0])

    return results


if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    projects = list(map(str, input().split(" ")))

    students = []
    for i in range(n):
        stu = list(map(str, input().split(" ")))
        students.append(stu)

    kemu = input().strip()

    print(" ".join(solution(projects, students, kemu)))

