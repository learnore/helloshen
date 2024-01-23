# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 查找树中元素
  Description :

🎃题目描述
已知树形结构的所有节点信息，现要求根据输入坐标(x,y)找到该节点保存的内容值，其中x表示节点所在的层数，根节点位于第0层，根节点的子节点位于第1层，依次类推； y表示节点在该层内的相对偏移，从左至右，第一个节点偏移0，第二个节点偏移1，依次类推；
在这里插入图片描述
如：上图中，假定圆圈内的数字表示节点保存的内容值，根据坐标（1,1）查到的内容值是23

🎃输入输出
输入

每个节点以一维数组表示，所有节点信息构成二维数组，二维数组的0位置存放根节点；

表示单节点的一维数组中， 0位置保存内容值，后续位置保存子节点在二维数组中的索引位置。

对于上图中：

● 根节点的可以表示为{10, 1, 2}，

● 树的整体表示为 { {10.1,2}，{-21,3,4}，{23,5}，{14}，{35}， {66} }

查询条件以长度为2的一维数组表示，上图查询坐标为(1,1 )时表示为{1,1}

使用Java标准IO键盘输入进行录入时，
1、先录入节点数量
2、然后逐行录入节点
3、最后录入查询的位置

对于上述示例为：
6
10 1 2
-21 3 4
23 5
14
35
66
1 1

输出
查询到内容时，输出 {内容值}，查询不到时输出{}
上图中根据坐标(1,1)查询输出{23}，根据坐标(1,2)查询输出{}

🎃样例1
输入
6
10 1 2
-21 3 4
23 5
14
35
66
1 1
输出
{23}


🎃样例2
输入
14
0 1 2 3 4
-11 5 6 7 8
113 9 10 11
24 12
35
66 13
77
88
99
101
102
103
25
104
2 5
输出
{102}


🎃样例3
输入
14
0 1 2 3 4
-11 5 6 7 8
113 9 10 11
24 12
35
66 13
77
88
99
101
102
103
25
104
3 2
输出
{}

  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/1/21 20:46
-------------------------------------------------
"""
from collections import defaultdict
from queue import Queue


def get_tree(input_list):
    """ 构造树，多叉树 """
    tree = defaultdict(list)
    for i in range(len(input_list)):
        for j in i[1:]:
            tree[i[0]].append((input_list[j][0], x+1))

    return tree


def layer_tree(tree, root_value, x, y):
    """ 层次遍历，队列 """
    if x == 0 and y == 0:
        return root_value

    queue = Queue()
    queue.put(root_value)
    # TODO 层次遍历，怎么获取层次？


if __name__ == "__main__":
    n = int(input().strip())
    tree = []
    first_root = list(map(int, input().strip().split(" ")))
    root_value = first_root[0]
    tree.append(first_root)

    for i in range(1, n):
        tree.append(list(map(int, input().strip().split(" "))))

    x, y = map(int, input().strip().split(" "))

    tree = get_tree(tree)
    result = layer_tree(tree, root_value, x, y)
    print(result)

