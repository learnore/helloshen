# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 深度优先（DFS）
  Description : 与回溯框架相同
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/21 12:33
-------------------------------------------------
"""


class Solution:

    def __init__(self):
        self.res = False

    def exist(self, board, word: str) -> bool:
        """
        解题思路：
        1、可以从任意点开始
        2、向上下左右扩散 dfs，不可走回头路
        """
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                # 第一个字母相同时，开始 dfs 遍历
                if board[i][j] == word[0]:
                    self.dfs(board, i, j, n, m, word, 0, [])

        return self.res

    def dfs(self, board, i, j, n, m, word, k, path):
        if len(path) == len(word):
            self.res = True
            return

        if self.res:
            return

        if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[k]:
            return

        # 做选择 + 做标记（避免走回头路）
        path.append(board[i][j])
        board[i][j] = '-' + board[i][j]
        k += 1
        # 继续选择
        self.dfs(board, i + 1, j, n, m, word, k, path)
        self.dfs(board, i - 1, j, n, m, word, k, path)
        self.dfs(board, i, j + 1, n, m, word, k, path)
        self.dfs(board, i, j - 1, n, m, word, k, path)
        # 撤销选择 + 撤销标记
        path.pop()
        board[i][j] = board[i][j][1]
        k -= 1


if __name__ == "__main__":
    solute = Solution()
    solute.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")
