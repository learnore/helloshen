# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : login_system
  Description : 登录 + 查询任务状态 + 统计任务状态
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/5/6 23:59
-------------------------------------------------
"""
import copy

from tools.ruoyi.common import post_request, login_interface, post_headers, task_interface, get_request, get_headers, \
    task_status_dict

if __name__ == "__main__":
    """ 登录获取 token """
    post_data = {
        "username": "zy-z82",  # zy-z82,syr-z16648
        "password": "5f14k#",
        "code": "0",  # TODO
        "uuid": "5c1f2cee86794ec2a840b58955b21585"  # data_dict["uuid"]     # TODO
    }

    login_data = post_request(login_interface, **post_data)

    token = login_data["token"]
    post_headers(token)  # headers 加入 token
    print(get_headers())

    """ 获取任务信息 """
    page_num, page_size, statistics_total = 1, 20, 0  # statistics_total 本次统计数量
    my_statistics = copy.deepcopy(task_status_dict)  # 深拷贝复制

    while True:
        params = {
            "pageNum": page_num,
            "pageSize": page_size,
            "taskStatusList": [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29,
                               30, 31, 32, 33, 34, 35, 95, 98]
        }  # 98: "错题确认中" 排除统计范围
        task_data = get_request(task_interface, params=params)
        print(task_data)

        # 如果已经找满了数据就开溜（但是中途可能会加入数据，所以尽可能在查询的时候先不要动后台）
        if statistics_total == task_data["total"]:
            break

        # 开始逐一分析数据
        for row in task_data["rows"]:
            statistics_total += 1

            task_id, task_status = row["questionId"], row["taskStatus"]  # 任务ID、任务状态
            task_statistics = my_statistics.get(task_status, "task_status_name:0")

            if len(task_statistics.split(":")) == 2:
                task_status_name, task_status_num = task_statistics.split(":")[0], int(
                    task_statistics.split(":")[1]) + 1
                my_statistics[task_status] = f"{task_status_name}:{task_status_num}"

            else:
                my_statistics[task_status] = f"{my_statistics[task_status]}:1"  # 第一次查到的时候，给个初始值 1

        # 页数自增
        page_num += 1

    # 移除没有统计的任务状态数据
    temp_tatistics = copy.deepcopy(my_statistics)  # 深拷贝
    for key, value in temp_tatistics.items():
        if len(value.split(":")) == 1:
            removed_value = my_statistics.pop(key)  # 移除 'key' 及其对应的值，并返回被移除的值

    print(f"\n总计\t{statistics_total} \n--------------------")
    for val in my_statistics.values():
        print(val)

    """ ------- 例子 -----
     - 本次统计数据如下
     总计	44 
     - 详细信息如下:
    审核待指派:10
    待审核:2
    审核问题待确认:4
    品检待分配:9
    待稽核:1
    效果审核通过:9
    错题确认中:9
    """


