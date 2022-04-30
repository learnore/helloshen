# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_array 数组
  Description : 虽然列表既灵活又简单，但面对各类需求时，我们可能会有更好的选择。比如，要存放
                1000 万个浮点数的话，数组（array）的效率要高得多，因为数组在背后存的并不是 float
                对象，而是数字的机器翻译，也就是字节表述。

                *** time 中的 perf_counter 方法，可以直接用来统计时间 ***
  Author      : chenyushencc@gmail.com
  date        : 2022/4/30 21:56
-------------------------------------------------
"""
import numpy
from array import array
from random import random
from time import perf_counter as pc


if __name__ == '__main__':
    floats = array('d', (random() for i in range(10**7)))   # 双精度浮点数组（类型码是 'd'）
    print(floats[-1])

    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()

    floats2 = array('d')
    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp, 10**7)
    fp.close()
    print(floats2[-1])
    print(floats2 == floats)

    # ------------------------------------------------------------------------------------

    """
    * memoryview.cast 会把同一块内存里的内容打包成一个全新的 memoryview 对象给你
    """
    numbers = array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)  # 利用含有 5 个短整型有符号整数的数组（类型码是 'h'）创建一个 memoryview
    print(len(memv))
    print(memv[0])              # memv 里的 5 个元素跟数组里的没有区别
    memv_oct = memv.cast('B')   # 创建一个 memv_oct，这一次是把 memv 里的内容转换成 'B' 类型，也就是无符号字符
    print(memv_oct.tolist())    # 以列表的形式查看 memv_oct 的内容
    memv_oct[5] = 4             # 把位于位置 5 的字节赋值成 4
    print(numbers)              # 因为我们把占 2 个字节的整数的高位字节改成了 4，所以这个有符号整数的值就变成了 1024

    # ------------------------------------------------------------------------------------

    """
    * NumPy 和 SciPy 提供的高阶数组和矩阵操作
    * NumPy 实现了多维同质数组（homogeneous array）和矩阵
    * SciPy 是基于 NumPy 的另一个库，它提供了很多跟科学计算有关的算法，专为线性代数、数值积分和统计学而设计
    * SciPy 的高效和可靠性归功于其背后的 C 和 Fortran 代码，而这些跟计算有关的部分都源自于 Netlib 库
    """
    a = numpy.arange(12)
    print(a)
    print(type(a))
    print(a.shape)      # 看看数组的维度，它是一个一维的、有 12 个元素的数组。
    a.shape = 3, 4
    print(a)
    print(a[2])
    print(a[2, 1])
    print(a[:, 1])      # 把第 1 列打印出来
    a.transpose()       # 把行和列交换，就得到了一个新数组
    print(a)

    floats = numpy.loadtxt('floats-10M-lines.txt')      # 从文本文件里读取 1000 万个浮点数
    print(floats[-3:])                                  # 利用序列切片来读取其中的最后 3 个数
    floats *= .5
    print(floats[-3:])
    t0 = pc()
    floats /= 3
    print(pc() - t0)
    numpy.save('floats-10M', floats)                    # 把数组存入后缀为 .npy 的二进制文件
    floats2 = numpy.load('float-10M.npy', 'r+')         # 将上面的数据导入到另外一个数组里，这次 load 方法利用了一种叫作内存映射的机制，它让我们在内存不足的情况下仍然可以对数组做切片
    floats2 *= 6
    print(floats2[-3])

