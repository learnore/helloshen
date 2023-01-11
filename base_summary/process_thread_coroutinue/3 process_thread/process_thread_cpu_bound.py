# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : process_thread_cpu_bound
  Description : 比较 单线程、多线程、多进程 运行 CPU 密集型计算（素数的判断）
  Author      : chenyushencc@gmail.com
  date        : 2023/1/11 15:08
-------------------------------------------------
"""
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


PRIMES = [112272535095293] * 100

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n%i == 0:
            return False

    return True


def single_thread():
    for number in PRIMES:
        is_prime(number)


def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime, PRIMES)


if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread used ", end-start, " s")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread used ", end - start, " s")

    start = time.time()
    multi_process()
    end = time.time()
    print("multi_process used ", end - start, " s")

    # 运行结果
    """
    single_thread used  138.29488801956177  s
    multi_thread used  136.42407178878784  s
    multi_process used  68.29880094528198  s
    """
