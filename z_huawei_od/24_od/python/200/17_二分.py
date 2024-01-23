# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 17
  Description :

🎃题目描述
某公司部门需要派遣员工去国外做项目，现在，代号为x的国家和代号为y的国家分别需要cntx名和cnty名员工，部门每个员工有一个员工号(1，2，3…)，工号连续，从1开始

部长派遣员工的规则：

1、从[1，k]中选择员工派遣出去
2、编号为x的倍数的员工不能去x国；编号为y的倍数的员工不能去y国

问题：找到最小的k，使得可以将编号在[1，k]中的员工分配给x国和y国，且满足x国和y国的需求

🎃输入输出
输入
四个整数 x，y， cntx，cnty；
(2<=x<y<=30000；x和y一定是质数；1<=cntx，cnty<10 ^ 9 ； cntx+cnty<=10^9)

输出
满足条件的最小的k

🎃样例1
输入
2 3 3 1
输出
5
说明:
输入说明:
2-表示国家代号2
3-表示国家代号3
3-表示国家2需要3个人
1-表示国家3需要1个人

  Summary     : 1、质数 = 素数，且大于1
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/23 15:25
-------------------------------------------------
"""


def is_valid(k, x, y, cntx, cnty):
    """
    判断给定的k是否能够满足x国和y国的需求。
    :param k: 当前考虑的员工编号上限
    :param x: x国的国家代号
    :param y: y国的国家代号
    :param cntx: x国需要的员工数量
    :param cnty: y国需要的员工数量
    :return: 如果能够满足需求则返回True，否则返回False
    """
    # 不能去x国的员工数量
    not_x = k // x
    # 不能去y国的员工数量
    not_y = k // y
    # 不能去x国和y国的员工数量
    not_both = k // (x * y)
    # 可以去x国的员工数量
    can_go_x = k - not_x
    # 可以去y国的员工数量
    can_go_y = k - not_y
    # 既可以去x国也可以去y国的员工数量
    can_go_both = k - not_x - not_y + not_both
    # 需要确定是否能够只通过这些员工满足两个国家的需求
    # 优先考虑去x国的员工数量，因为我们总是可以从既能去x国又能去y国的员工中挑选出一些去y国
    if can_go_x >= cntx and can_go_y >= cnty and can_go_x + can_go_both >= cntx and can_go_y + can_go_both >= cnty:
        return True

    return False


def find_minimum_k(x, y, cntx, cnty):
    """
    使用二分查找的方法来确定最小的k值。
    :param x: x国的国家代号
    :param y: y国的国家代号
    :param cntx: x国需要的员工数量
    :param cnty: y国需要的员工数量
    :return: 满足条件的最小的k值
    """
    left, right = 1, 2 * (cntx + cnty)  # 初始的搜索范围，保证足够大
    result = right  # 存储最终结果，初始为最大可能值
    while left <= right:
        mid = left + (right - left) // 2  # 计算中间值
        if is_valid(mid, x, y, cntx, cnty):
            result = min(result, mid)  # 更新结果为更小的k值
            right = mid - 1  # 继续搜索更小的k值
        else:
            left = mid + 1  # 搜索更大的k值
    return result


if __name__ == "__main__":
    # 读取输入
    x, y, cntx, cnty = map(int, input().split())
    # 输出结果
    print(find_minimum_k(x, y, cntx, cnty))
