# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : base_paython
  Description : 解题技巧
                字符串判断：可用 for + if + 字符串作数组
                如 HJ40 统计字符：https://www.nowcoder.com/practice/539054b4c33b4776bc350155f7abd8f5?tpId=37&tqId=21263&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D100%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=

  Author      : chenyushencc@gmail.com
  date        : 2023/2/3 12:17
-------------------------------------------------
"""
import heapq
import math

if __name__ == "__main__":
    """
    字符串
    """
    # 字符串去除前后空格
    print(" 1 2 3 ".strip())        # 1 2 3

    # 字符串前后关键字符判别
    print("123!".endswith("!"))         # True
    print("123!".startswith("12"))      # True

    # 数组 字符串 是可以使用 .count() 进行计数的
    print(["1", "1", "3"].count("1"))       # 2
    print("1231".count("1"))                # 2

    # 字符串左对其
    print("123".ljust(8, "0"))  # 12300000
    print("123".rjust(8, "0"))  # 00000123

    # 字符串可以取超过自身的区间，超过部分会自动忽略的
    print("123"[:100])

    # 求开根号
    print(math.sqrt(100))       # 10.0

    # print 的其他用法
    print("123", end=" 12\n")

    """
    常用数值计算
    """
    # 向下取整
    print(int(3.56))        # 3
    # 向上取整
    print(math.ceil(3.25))  # 4
    # 四舍五入
    print(round(4.5), round(5.5), round(6.5), round(7.5))     # 4 6 6 8     TODO 坑-round 奇进偶舍，4 6 是偶数直接舍弃  5，7是奇数
    print(round(4.3), round(5.3), round(6.3), round(7.3))     # 4 5 6 7


    """
    执行表达式
    """
    print(eval("300+4/2"))      # 302.0

    """
    range 的逆向使用，注意：前面的两个范围参数，第一个的值 > 第二个的值，第三个参数为 负数 才有意义
    """
    for i in range(10, -1, -1):
        print(i)

    """
    字母大小写，判断时可以有其他杂质
    """
    print("asdASD".lower())     # asdasd
    print("asdASD".islower())   # False
    print("asdASD".upper())     # ASDASD
    print("123^%$&*$$(ASDASD".isupper())   # True

    """
    素数/质数的判断逻辑：不能被从2开始到自己前一个数整除即可
    """
    def is_sushu(n):
        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    """ 
    数组
    """
    my_arr = [4,5] + [1,2,3]    # [4,5].extend([1,2,3])
    print(my_arr)               # [4, 5, 1, 2, 3]
    arr1 = [4,5]
    arr2 = [1,2,3]
    arr1.extend(arr2)
    print(arr1)                 # [4, 5, 1, 2, 3]
    print([4,5].extend([1,2,3]))    # extend 只是一个扩充的“动作”，是没有返回值的，所以 结果是 None

    """
    zip 两个数组一一对应打包成元组
    """
    height = [1, 3, 5, 7, 9]
    weight = [2, 4, 6, 8, 10]
    print(zip(height, weight))            # <zip object at 0x0000017B313DB200>
    print(list(zip(height, weight)))      # [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    # xxxxxxxxxxxxxxxxxxxxxxxx 一般人 xxxxxxxxxxxxxxxxxxxxxxxx
    people = []
    for i in range(len(height)):
        people.append((height[i], weight[i]))
    print(people)                         # [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

    """
    堆栈：注意，不管是 heapify heappush heappop 都必须带上指定的 min_heapq 参数
    """
    min_heapq = []
    heapq.heapify(min_heapq)       # 小堆化

    heapq.heappush(min_heapq, 3)    # 进堆
    heapq.heappush(min_heapq, 1)    # 进堆
    heapq.heappush(min_heapq, 2)    # 进堆

    heapq.heappop(min_heapq)        # 出堆 [1,2,3] 出1
    heapq.heappop(min_heapq)        # 出堆 [2,3]  出2
    print(min_heapq)                # [3]
    # TODO 思维/小技巧：如果是想使用 大堆 的话，将值取负就可以了！！！

    """
    数组 最大值 & 最大值的索引（多个返回第一个）
    """
    my_arr_max = [1, 2, 3, 6, 6, 4, 5]
    print(max(my_arr_max))      # 6
    print(my_arr_max.index(max(my_arr_max)))        # 3 多个返回第一个