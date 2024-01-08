# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 二叉树
  Description :
  Summary     :
    1、递归时，考虑 if not root 的情况
    2、

  Author      : chenyushencc@gmail.com
  date        : 2023/2/6 13:59
-------------------------------------------------
"""

"""
https://www.nowcoder.com/practice/508378c0823c423baa723ce448cbfd0c

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
226. 翻转二叉树
https://leetcode.cn/problems/invert-binary-tree/description/
"""
class Solution:
    def invertTree(self, root):
        # base case
        if not root:
            return

        # left right 交换
        temp = root.left
        root.left = root.right
        root.right = temp

        # 子树反转
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


"""
114. 二叉树展开为链表（中等）
https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/
"""
class Solution:
    def flatten(self, root) -> None:
        # 使用递归的思想，自己要明确本函数的定义：将root变成right子孩子的单链表
        if not root:
            return

        self.flatten(root.left)  # 将左子树变成只有右单链表的格式
        self.flatten(root.right)  # 将右子树变成只有右单链表的格式

        left_child, right_child = root.left, root.right  # 此时左右子树已经都是右单链的格式了

        # 先将左子树清空，并将左子树放在 右子树上
        root.left = None
        root.right = left_child

        # 再将指针指到右子树的尾部，将尾部指向原本的右子树即可
        dummy = root
        while dummy.right:
            dummy = dummy.right
        dummy.right = right_child


"""
116. 填充每个节点的下一个右侧节点指针（中等）
https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/description/
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return

        self.node_next(root.left, root.right)
        return root

    def node_next(self, node1, node2):
        if not node1 or not node2:
            return

        node1.next = node2
        # 各自的左右子树
        self.node_next(node1.left, node1.right)
        self.node_next(node2.left, node2.right)

        # 右子树 next 指向左子树
        self.node_next(node1.right, node2.left)


"""
654. 最大二叉树（中等）
https://leetcode.cn/problems/maximum-binary-tree/
"""
class Solution:
    def constructMaximumBinaryTree(self, nums):
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, low, high):
        if low > high:
            return

        # 找出数组 low:high+1 区间中的最大值和最大值的索引（注意[:]法则，顾前不顾后，所以要 high+1）
        max_value = max(nums[low:high + 1])  # WARNING
        max_index = nums.index(max_value)

        # 构造二叉树
        root = TreeNode(val=max_value)
        root.left = self.build(nums, low, max_index - 1)
        root.right = self.build(nums, max_index + 1, high)
        return root


"""
105. 从前序与中序遍历序列构造二叉树（中等）
https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
class Solution:
    def buildTree(self, preorder, inorder):
        # 利用前序遍历根结点的下一个值就是下一个根节点
        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        if pre_start > pre_end:
            return

        root_value = preorder[pre_start]
        if pre_start == pre_end:
            return TreeNode(val=root_value)

        root_index = inorder[in_start:in_end + 1].index(root_value) + in_start      # 这里记得 + in_start 偏移量
        left_len = root_index - in_start

        root = TreeNode(val=root_value)
        root.left = self.build(preorder, pre_start + 1, pre_start + 1 + left_len - 1, inorder, in_start,
                               root_index - 1)  # 注意这里的 pre_end 位置是 pre_start+1+left_len-1 最后是 -1 不是 +1，想不明白可以画个图
        root.right = self.build(preorder, pre_start + 1 + left_len - 1 + 1, pre_end, inorder, root_index + 1, in_end)
        return root


"""
106. 从中序与后序遍历序列构造二叉树（中等）
https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
"""
class Solution:
    """
    单链，最容易不通过的例子：
    inorder = [1,2,3,4]
    postorder = [4,3,2,1]
    """

    def buildTree(self, inorder, postorder):
        return self.build(postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1)

    def build(self, postorder, post_start, post_end, inorder, in_start, in_end):
        if post_start > post_end:
            return

        root_value = postorder[post_end]
        if post_start == post_end:
            return TreeNode(val=root_value)

        # root 值在中序排序中的 index（[:]顾前不顾后的原则别忘了in_end+1）
        root_index = inorder[in_start:in_end + 1].index(root_value) + in_start  # 注意偏移量
        left_len = root_index - in_start

        root = TreeNode(val=root_value)
        root.left = self.build(postorder, post_start, post_start + left_len - 1, inorder, in_start,
                               root_index - 1)  # post_start+left_len-1 是 -1
        root.right = self.build(postorder, post_start + left_len - 1 + 1, post_end - 1, inorder, root_index + 1, in_end)
        return root


"""
652. 寻找重复的子树（中等）
https://leetcode.cn/problems/find-duplicate-subtrees/description/
"""
class Solution:

    def __init__(self):
        self.sub_strs = {}
        self.res = []

    def findDuplicateSubtrees(self, root):
        self.build(root)
        return self.res

    def build(self, root):
        if not root:
            return "#"

        left = self.build(root.left)
        right = self.build(root.right)

        # 前序遍历记录（可用）
        sub_tree = str(root.val) + "," + left + "," + right
        # 中序遍历记录（不可用xxxxxxxxxxxxxxxxxxx）
        # sub_tree = left + "," + str(root.val) + "," + right
        # 后序遍历记录（可用）
        # sub_tree = left + "," + right + "," + str(root.val)

        if sub_tree in self.sub_strs:
            self.sub_strs[sub_tree] += 1
        else:
            self.sub_strs[sub_tree] = 1

        freq = self.sub_strs[sub_tree]
        if freq == 2:  # 只在 = 2 时记录，超过2或者不足2都不再记录
            self.res.append(root)
        return sub_tree


"""
（不设置序列化和反序列化的规则？？？？？）297. 二叉树的序列化与反序列化
https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/description/
"""
from queue import Queue
class Codec:
    """ 解法一：前序遍历 """

    def __init__(self):
        self.sub_str = ""

    def serialize(self, root):
        """ 序列化 """
        sub_str = ""
        self.serialize_tree(root)
        return self.sub_str

    def serialize_tree(self, root):
        if not root:
            self.sub_str += "NULL" + ","  # 精髓，处理虚拟的
            return None

        """ 前序遍历 """
        self.sub_str += str(root.val) + ","
        self.serialize_tree(root.left)
        self.serialize_tree(root.right)

    # --------------------------------------------------------------------
    def deserialize(self, data):
        """ 反序列化 """
        sub_tree_arr = data.split(",")
        return self.deserialize_str(sub_tree_arr)

    def deserialize_str(self, sub_tree_arr):
        if not len(sub_tree_arr):
            return None

        """ 这三步的顺序不要搞反！！！ """
        first = sub_tree_arr[0]
        sub_tree_arr.pop(0)  # 移除第一个元素 等价于 sub_tree_arr.remove(first)
        if first == "NULL" or first == "":
            return None

        """ 前序遍历 """
        root = TreeNode(val=first)
        root.left = self.deserialize_str(sub_tree_arr)
        root.right = self.deserialize_str(sub_tree_arr)
        return root


"""
1373. 二叉搜索子树的最大键值和
https://leetcode.cn/problems/maximum-sum-bst-in-binary-tree/description/
"""
class Solution:
    def __init__(self):
        self.max_value = 0

    def maxSumBST(self, root):
        self.build(root)
        return self.max_value

    def build(self, root):
        if not root:
            """
            [0] 是否是二叉树
            [1] 二叉树中的最大值(因为二叉搜索树的右子树最大值也得大于根节点)
            [2] 二叉树中的最小值(因为二叉搜索树的左子树最小值也得小于根节点)
            [3] 子树的和
            """
            return [1, -40000, 40000, 0]

        left = self.build(root.left)
        right = self.build(root.right)

        res = [0, 0, 0, 0]
        # 要满足二叉搜索树的基本要求，左子树的所有节点都要小于根节点（右子树的所有子节点都要大于根节点）
        if left[0] == 1 and right[0] == 1 and left[1] < root.val and right[2] > root.val:
            res[0] = 1
            res[1] = max(root.val, right[1])
            res[2] = min(root.val, left[2])
            res[3] = left[3] + right[3] + root.val

            self.max_value = max(self.max_value, res[3])

        return res


"""
104. 二叉树的最大深度
https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/
"""
class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1


"""
543. 二叉树的直径
https://leetcode.cn/problems/diameter-of-binary-tree/description/
"""
class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root):
        # 本题注意：两结点之间的路径长度是以它们之间边的数目表示
        self.max_depth(root)
        return self.res

    def max_depth(self, root):
        if not root:
            return 0

        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        # 注意：两结点之间的路径长度是以它们之间边的数目表示
        self.res = max([self.res, left_depth + right_depth])

        return max(left_depth, right_depth) + 1


"""
144. 二叉树的前序遍历
https://leetcode.cn/problems/binary-tree-preorder-traversal/description/
"""
class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root):
        if not root:
            return []

        self.res.append(root.val)  # 前序遍历
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.res


if __name__ == "__main__":
    pass
