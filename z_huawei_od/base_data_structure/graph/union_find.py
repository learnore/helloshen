# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : Union_Find
  Description : 并查集 (ChatGPT 更改 Java 代码)
  Summary     : 1、优化一：在 union 时，小树接到大树下面，保持平衡，避免树变成单边树，从而降低时间复杂度
                2、优化二：路径压缩，在每次 find 时，将树的子结点，都尽可能指向根节点，时间复杂度变成 O(1)
                3、建议，直接背下来，这就是最优化的模板
  Author      : chenyushencc@gmail.com
  date        : 2024/1/10 20:03
-------------------------------------------------
"""


class UnionFind:
    def __init__(self, n):
        # 连通分量个数
        self.count = n
        # 存储每个元素的根节点
        self.parent = [i for i in range(n)]
        # 记录每棵树的“重量”
        self.size = [1] * n

    def union(self, p, q):
        # 找到每个元素的根节点
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return False

        # 优化一：小树接到大树下面，保持平衡
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1
        return True

    def connected(self, p, q):
        # 检查两个元素是否连通
        return self.find(p) == self.find(q)

    def find(self, x):
        # 找到元素所属树的根节点
        while self.parent[x] != x:
            # 优化二：路径压缩
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

# 示例用法:
# n = 10  # 替换为所需的大小
# uf = UF(n)
# uf.union(0, 1)
# uf.union(2, 3)
# print(uf.connected(0, 1))  # 应打印 True
# print(uf.connected(0, 2))  # 应打印 False
