# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : common
  Description : 
  Summary     : 1、
                2、
                3、
  Author      : chenyushencc@gmail.com
  date        : 2024/5/7 19:25
-------------------------------------------------
"""
import requests
import json


http_url = "https://book-video-admin.eebbk.net"

token = 'your_token_here'

captcha_image_interface = "/book-video-admin/captchaImage"    # 获取验证码的图片接口
login_interface = "/book-video-admin/login"


def get_request(interface_name, headers=None):
    """ get 请求公共方法 """
    response = requests.get(http_url + interface_name)  # 发送GET请求
    response_string = response.text  # response.text 是一个包含JSON格式数据的字符串

    print(f"{interface_name}: {response.status_code}")      # 打印状态码
    return json.loads(response_string)  # 将JSON字符串解析为Python字典


def post_request(interface_name, **data):
    """ post 请求公共方法 """

    # data = {'key': 'value'}
    response = requests.post(http_url + interface_name, data=data)
    print(f"{interface_name}: {response.status_code}")      # 打印状态码



def post_token(new_token):
    """ 修改 token """
    token = new_token


def get_token():
    """ 获取 token """
    return token


if __name__ == "__main__":
    print("chenyushen")
