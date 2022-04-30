# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_collections
  Description : collections.deque 类（双向队列）是一个线程安全、可以快速从两端添加或者删除元素的
                数据类型。

                queue
                    提供了同步（线程安全）类 Queue、LifoQueue 和 PriorityQueue，不同的线程可以利用
                    这些数据类型来交换信息。这三个类的构造方法都有一个可选参数 maxsize，它接收正
                    整数作为输入值，用来限定队列的大小。但是在满员的时候，这些类不会扔掉旧的元素
                    来腾出位置。相反，如果队列满了，它就会被锁住，直到另外的线程移除了某个元素而
                    腾出了位置。这一特性让这些类很适合用来控制活跃线程的数量。

                multiprocessing
                    这个包实现了自己的 Queue，它跟 queue.Queue 类似，是设计给进程间通信用的。同时
                    还有一个专门的 multiprocessing.JoinableQueue 类型，可以让任务管理变得更方便。

                asyncio
                    Python 3.4 新提供的包，里面有 Queue、LifoQueue、PriorityQueue 和 JoinableQueue，
                    这些类受到 queue 和 multiprocessing 模块的影响，但是为异步编程里的任务管理提供
                    了专门的便利。

                heapq
                    跟上面三个模块不同的是，heapq 没有队列类，而是提供了 heappush 和 heappop 方法，
                    让用户可以把可变序列当作堆队列或者优先队列来使用。
  Author      : chenyushencc@gmail.com
  date        : 2022/4/30 23:27
-------------------------------------------------
"""
from collections import deque

if __name__ == '__main__':
    """
    * append 和 popleft 都是原子操作，也就说是 deque 可以在多线程程序中安全地当作先进先出的队列使用，而使用者不需要担心资源锁的问题。
    """
    dq = deque(range(10), maxlen=10)    # maxlen 是一个可选参数，代表这个队列可以容纳的元素的数量，而且一旦设定，这个属性就不能修改了
    print(dq)       # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
    dq.rotate(3)    # 队列的旋转操作接受一个参数 n，当 n > 0 时，队列的最右边的 n 个元素会被移动到队列的左边。当 n < 0 时，最左边的 n 个元素会被移动到右边
    print(dq)       # deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
    dq.rotate(-4)
    print(dq)           # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
    dq.appendleft(-1)   # 当试图对一个已满（len(d) == d.maxlen）的队列做头部添加操作的时候，它尾部的元素会被删除掉。注意在下一行里，元素 0 被删除了
    print(dq)           # deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
    dq.extend([11, 22, 33])     # 在尾部添加 3 个元素的操作会挤掉 -1、1 和 2
    print(dq)                   # deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
    dq.extendleft([10, 20, 30, 40])     # extendleft(iter) 方法会把迭代器里的元素逐个添加到双向队列的左边，因此迭代器里的元素会逆序出现在队列里
    print(dq)                           # deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
