# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : login_system
  Description : 
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/5/6 23:59
-------------------------------------------------
"""
from tools.ruoyi.common import post_request, login_interface, post_headers, task_interface, get_request, get_headers

if __name__ == "__main__":
    post_data = {
        "username": "syr-z1黄晓英6648",
        "password": "",
        "code": "5",            # TODO
        "uuid": "8bb98a0d1d994bd0856e8d86baf6b5b2"            # data_dict["uuid"]
    }

    login_data = post_request(login_interface, **post_data)

    token = login_data["token"]
    post_headers(token)     # headers 加入 token
    print(get_headers())


    params = {
        "pageNum": 1,
        "pageSize": 10,
        "taskStatusList": [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 95, 98]
    }
    task_data = get_request(task_interface, params=params)
    print(task_data)


