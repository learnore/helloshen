# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : 03 flask_thread_pool
  Description : flask + 线程池，用 postman 测试
  Author      : chenyushencc@gmail.com
  date        : 2023/1/11 14:26
-------------------------------------------------
"""
import json
import time
import flask
from concurrent.futures import ThreadPoolExecutor       # 引入线程池


app = flask.Flask(__name__)
pool = ThreadPoolExecutor()     # 定义线程池


def read_file():
    time.sleep(0.1)
    return "read_file"


def read_db():
    time.sleep(0.2)
    return "read_db"


def read_api():
    time.sleep(0.3)
    return "read_api"


@app.route("/")
def index():
    result_file = pool.submit(read_file)        # 使用线程池 pool.submit
    result_db = pool.submit(read_db)            # 使用线程池 pool.submit
    result_api = pool.submit(read_api)          # 使用线程池 pool.submit

    return json.dumps({
        "result_file": result_file.result(),    # 返回线程池结果 pool.result
        "result_db": result_db.result(),
        "result_api": result_api.result()
    })


if __name__ == "__main__":
    app.run()
