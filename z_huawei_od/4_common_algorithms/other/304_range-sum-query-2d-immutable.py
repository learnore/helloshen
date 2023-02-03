# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 304_range-sum-query-2d-immutable
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2023/2/3 10:54
-------------------------------------------------
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)  # 行数
        n = len(matrix[0])  # 列数

        """ 初始化 0（行 列 +1） """
        self.pre_num = []
        for i in range(m + 1):
            temp = []
            for j in range(n + 1):
                temp.append(0)
            self.pre_num.append(temp)

        """ 二维矩阵，构造前缀和 """
        for i in range(1, m + 1):  # 从 1 开始
            for j in range(1, n + 1):  # 从 1 开始
                # TODO 右上角斜线相加，减去左上角，再加上自己位置的数值
                self.pre_num[i][j] = self.pre_num[i - 1][j] + self.pre_num[i][j - 1] - self.pre_num[i - 1][j - 1] + \
                                     matrix[i - 1][j - 1]

        # print(self.pre_num)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_num[row2 + 1][col2 + 1] - self.pre_num[row1][col2 + 1] - self.pre_num[row2 + 1][col1] + \
               self.pre_num[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == "__main__":
    pass
