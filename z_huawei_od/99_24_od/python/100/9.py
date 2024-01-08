# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 9
  Description :

-------- 示例 --------
输入
2 8 3 7 3 6 3 5 4 4 5 3 6 2 7 3 8 4 7 5
输出
2 8 3 7 3 5 6 2 8 4 7 5

  Summary     : 1、坐标少于3个，则全部返回
                2、开始结点和结尾结点，必在返回结果中
                3、拐点的判断：当前结点与前后结点是否共线，共线则不是拐点，则不用加入
                4、共线的判断用到了线代的 "平行向量之比相等" 知识点

  Author      : chenyushencc@gmail.com
  date        : 2024/1/8 9:44
-------------------------------------------------
"""


def is_turning_point(p1, p2, p3):
    """
    判断点p2是否为拐点。
    如果p1、p2、p3三点不在同一条直线上，则p2为拐点。
    :param p1: 第一个点的坐标 (row, col)
    :param p2: 第二个点的坐标 (row, col)
    :param p3: 第三个点的坐标 (row, col)
    :return: p2是否为拐点的布尔值
    """
    # 通过计算向量的叉积来判断是否共线
    # 向量p1p2和向量p2p3的叉积如果不为0，则三点不共线，p2为拐点
    """
    叉积，线代，用于判断三点是否共线
    可以理解为三点中，任意两点相减组成向量，是否平行
    (p1[0], p1[1])
    (p2[0], p2[1])
    (p3[0], p3[1])
    
    向量一：(p3[0] - p2[0], p3[1] - p2[1])
    向量二：(p2[0] - p1[0], p2[1] - p1[1])
    两向量之比，相等就是平行的
    p3[0] - p2[0]               p3[1] - p2[1]
    -------------       =       -------------
    p2[0] - p1[0]               p2[1] - p1[1]
    
    故有：p3[1] - p2[1]) * (p2[0] - p1[0])     =     (p3[0] - p2[0]) * (p2[1] - p1[1])
    
    """
    return (p3[1] - p2[1]) * (p2[0] - p1[0]) != (p3[0] - p2[0]) * (p2[1] - p1[1])


def simplify_coordinates(coords):
    """
    简化坐标列表，移除冗余点。
    :param coords: 包含有冗余数据的坐标列表
    :return: 简化后的坐标列表
    """
    # 至少需要三个点来判断拐点，因此如果点的数量不足三个，直接返回原坐标列表
    if len(coords) < 6:
        return coords
    # 将输入的一维坐标列表转换为二维列表，每个元素是一对坐标
    points = [(coords[i], coords[i + 1]) for i in range(0, len(coords), 2)]
    # 存储简化后的坐标点
    simplified = [points[0]]  # 起点一定是关键点
    # 遍历输入的坐标点，检查每个点是否为拐点
    for i in range(1, len(points) - 1):
        # 如果当前点是拐点，则将其加入到简化后的坐标列表中
        if is_turning_point(points[i - 1], points[i], points[i + 1]):
            simplified.append(points[i])
    # 终点一定是关键点
    simplified.append(points[-1])
    # 将二维坐标列表转换为一维列表，以符合输出格式
    simplified_coords = [item for point in simplified for item in point]
    return simplified_coords


if __name__ == "__main__":
    # 读取输入数据
    input_coords = list(map(int, input().split()))
    # 简化坐标
    simplified_coords = simplify_coordinates(input_coords)
    # 输出简化后的坐标
    print(' '.join(map(str, simplified_coords)))