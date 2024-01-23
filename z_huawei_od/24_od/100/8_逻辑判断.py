# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 8
  Description :

-------- 示例 --------
输入
1
0 1
1 2
输出
3

-------- 示例 --------
输入
1
0 1
3 2
输出
1

-------- 示例 --------
输入
3
0 1
3 2
输出
5

-------- 示例(输出信息不合法，有区域重叠) --------
输入
3
0 1
0 1
输出
-1

-------- 示例(没有足够空间分配) --------
输入
1
0 1
1 99
输出
-1

  Author      : chenyushencc@gmail.com
  date        : 2024/1/7 21:29
-------------------------------------------------
"""


def allocate_memory(request_size, allocated_memory):

    # 初始化堆
    heap = [True for _ in range(100)]

    # 根据 allocated_memory 在数组中占用的部分 false 掉
    for i, item in enumerate(allocated_memory):
        offset, size = item
        for i in range(size):
            if heap[offset+i] == False:     # 如果已经设置了，那么就是重复设置，那就违反了第一条，申请失败
                return -1
            heap[offset+i] = False

    temp_request_size = request_size
    for i, item in enumerate(heap):
        if temp_request_size == request_size:
            last_offset = i

        if item == False:
            temp_request_size = request_size
            last_offset = 0
            continue
        else:
            temp_request_size -= 1

        if temp_request_size == 0:
            return last_offset

    return -1           # 没有足够空间分配


if __name__ == "__main__":
    request_size = int(input().strip())
    allocated_memory = []

    # for _ in range(2):
    #     offset, size = map(int, input().split())
    #     allocated_memory.append((offset, size))

    while True:
        try:
            offset, size = map(int, input().split())
            allocated_memory.append((offset, size))
        except EOFError:
            break

    result = allocate_memory(request_size, allocated_memory)
    print(result)
