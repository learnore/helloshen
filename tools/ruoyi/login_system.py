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
from tools.ruoyi.common import post_request, login_interface

if __name__ == "__main__":
    post_data = {
        "username": "syr-z1黄晓英6648",
        "password": "",
        "code": "48",            # TODO
        "uuid": "870552c4a8c74cd3af1ff8786c9724ae"            # data_dict["uuid"]
    }
    post_request(login_interface, **post_data)


