# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 1 API集群负载统计（简单判断）
  Description :

-------- 示例1 --------
输入
5
/huawei/computing/no/one
/huawei/computing
/huawei
/huawei/cloud/no/one
/huawei/wireless/no/one
3 no
输出
2

-------- 示例2 --------
5
/huawei/computing/no/one
/huawei/computing
/huawei
/huawei/cloud/no/one
/huawei/wireless/no/one
3 no
3

  Author      : chenyushencc@gmail.com
  date        : 2024/1/2 13:27
-------------------------------------------------
"""


def count_keyword_frequency(logs, level, keyword):
    """ 从一堆 logs 中，统计单个 log 的第 level 层是不是 keyword """
    frequency = 0
    for log in logs:
        # 将URL按照/分割成层级
        url_segments = log.split('/')

        # 检查层级是否足够，防止越界
        if len(url_segments) > level:
            # 获取指定层级的字符串
            target_segment = url_segments[level]

            # 判断关键字是否匹配
            if target_segment == keyword:
                frequency += 1

    return frequency


if __name__ == "__main__":
    # 输入
    N = int(input())
    logs = [input() for _ in range(N)]

    layer, keyword = map(str, input().split())
    layer = int(layer)

    result = count_keyword_frequency(logs, layer, keyword)

    # 输出
    print(result)

