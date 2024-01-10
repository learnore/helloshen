# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : flask_process_pool
  Description : 
  Author      : chenyushencc@gmail.com
  date        : 2023/1/11 20:09
-------------------------------------------------
"""
import json
import math
import flask
from concurrent.futures import ProcessPoolExecutor


process_pool = ProcessPoolExecutor()
app = flask.Flask(__name__)


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


@app.route("/is_prime/<number>")
def api_is_prime(number):
    number_list = [int(num) for num in number.split(",")]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))


if __name__ == "__main__":
    app.run()
