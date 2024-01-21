# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 1
  Description : 构建最小生成树（MST）
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/10 11:16
-------------------------------------------------
"""
from z_huawei_od.base_data_structure.graph.union_find import UnionFind


# 计算连接所有站点的最小成本
def min_cost_to_connect_stations(N, connections):
    uf, total_cost = UnionFind(N), 0

    # 首先处理已经存在的连接，不增加额外成本
    for x, y, cost, connected in connections:
        if connected == 1:          # 表示已连接
            uf.union(x - 1, y - 1)  # 开始连接，减1是因为并查集中节点索引是从0开始的

    # 选出所有未连接的边，按成本从低到高排序
    remaining_connections = [c for c in connections if c[3] == 0]       # if c[3] == 0 表示未连接
    remaining_connections.sort(key=lambda x: x[2])

    # 使用克鲁斯卡尔算法逐条检查未连接的边
    for x, y, cost, connected in remaining_connections:
        # 如果添加这条边不会造成循环，则添加到 MST 中
        if uf.union(x - 1, y - 1):
            total_cost += cost

    # 检查是否所有节点都已经连接在同一棵树上
    if uf.count > 1:        # 如果有超过 1 个的联通分量，那么就不是最小生成树
        return -1

    return total_cost


if __name__ == "__main__":
    # 读取输入数据
    N = int(input())
    M = int(input())
    connections = []
    for _ in range(M):
        x, y, z, p = map(int, input().split())
        connections.append((x, y, z, p))

    # 计算最小成本并输出
    min_cost = min_cost_to_connect_stations(N, connections)
    print(min_cost)
