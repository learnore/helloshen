# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : kuohao_questions
  Description : 括号问题 3 道秒杀
  Author      : chenyushencc@gmail.com
  date        : 2023/2/5 14:18
-------------------------------------------------
"""

"""
20. 有效的括号
https://leetcode.cn/problems/valid-parentheses/
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            else:
                if not len(stack):
                    return False

                if stack[-1] != self.duiying_kuohao(i):
                    return False

                stack.pop()

        if len(stack):
            return False
        else:
            return True

    def duiying_kuohao(self, kuohao):
        if kuohao == ")":
            return "("
        elif kuohao == "]":
            return "["
        else:
            return "{"


"""
921. 使括号有效的最少添加
https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/description/
"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_kuohao, right_kuohao = 0, 0
        for i in s:
            if i == "(":
                right_kuohao += 1
            else:
                right_kuohao -= 1
                if right_kuohao == -1:
                    right_kuohao = 0
                    left_kuohao += 1

        return left_kuohao + right_kuohao


"""
1541. 平衡括号字符串的最少插入次数
https://leetcode.cn/problems/minimum-insertions-to-balance-a-parentheses-string/description/
"""
class Solution:
    def minInsertions(self, s: str) -> int:
        left_kuohao, right_kuohao = 0, 0
        for i in s:
            if i == "(":
                right_kuohao += 2

                if right_kuohao % 2 == 1:
                    right_kuohao -= 1  # 注意
                    left_kuohao += 1
            else:
                right_kuohao -= 1

                if right_kuohao == -1:
                    right_kuohao = 1  # 注意
                    left_kuohao += 1

        return left_kuohao + right_kuohao


if __name__ == "__main__":
    pass
