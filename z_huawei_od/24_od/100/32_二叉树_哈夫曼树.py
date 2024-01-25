# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 32
  Description :

------------- 用例 -------------------
输入
5
5 15 40 30 10
输出
40 100 30 60 15 30 5 15 10

  Summary     : 1、生成哈夫曼的过程，用堆的数据结构
                2、class 中的 __lt__ 方法，用于解决同类型的 class 的比较问题
                    （TypeError: '<' not supported between instances of 'TreeNode' and 'TreeNode'）
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/17 11:17
-------------------------------------------------
"""

# Definition for a binary tree node.
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # 放入小根堆时，方便自身比较 ，不然发送错误 ：TypeError: '<' not supported between instances of 'TreeNode' and 'TreeNode'
    def __lt__(self, other):            # ****************
        return self.val < other.val


def huffman(input_list):
    """
    根据 input_list 数组，变成堆，每次选择2个最小的，生成一个
    变成一个最小数在左侧的哈夫曼树
    相同的数，在原来数组的在左侧
    """
    heap = [TreeNode(i) for i in input_list]        # 将每个数组元素变成树（此时每个树只有一个结点）
    heapq.heapify(heap)     # 将数组变成小根堆
    while len(heap) > 1:
        # 从小根堆中，依次出2个结点
        node_1 = heapq.heappop(heap)
        node_2 = heapq.heappop(heap)

        # 组成新的结点
        merged_tree = TreeNode(node_1.val + node_2.val)
        merged_tree.left = node_1           # 小的端点在左边
        merged_tree.right = node_2

        # 将新的结点加入堆中
        heapq.heappush(heap, merged_tree)

    return heap[0]


results = []
def in_tree(root):
    """ 中序遍历 """
    if not root:
        return

    in_tree(root.left)
    results.append(root.val)
    in_tree(root.right)


if __name__ == "__main__":
    n = int(input())
    input_list = list(map(int, input().split(" ")))

    root = huffman(input_list)
    in_tree(root)
    print(" ".join([str(i) for i in results]))
