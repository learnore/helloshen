# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : operator_functools
  Description : operator 模块中还有一类函数，能替代从序列中取出元素或读取对象属性的 lambda 表达式

  Author      : chenyushencc@gmail.com
  date        : 2022/5/6 22:50
-------------------------------------------------
"""
import functools
import unicodedata
from collections import namedtuple
from functools import reduce, partial
from operator import mul, itemgetter, attrgetter, methodcaller


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n+1))


def fact(n):
    return reduce(mul, range(1, n+1))


if __name__ == '__main__':
    metro_data = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
    ]
    for city in sorted(metro_data, key=itemgetter(1)):
        print(city)
        '''
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386))
        '''

    cc_name = itemgetter(1, 0)
    for city in metro_data:
        print(cc_name(city))
        '''
        ('JP', 'Tokyo')
        ('IN', 'Delhi NCR')
        ('MX', 'Mexico City')
        ('US', 'New York-Newark')
        ('BR', 'Sao Paulo')
        '''

    LatLong = namedtuple('LatLong', 'lat long')     # 使用 namedtuple 定义 LatLong
    Metropolis = namedtuple('Metropolis', 'name cc pop coord')
    metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
    print(metro_areas[0])   # Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722, long=139.691667))
    print(metro_areas[0].coord.lat)

    name_lat = attrgetter('name', 'coord.lat')
    for city in sorted(metro_areas, key=attrgetter('coord.lat')):
        print(name_lat(city))
        '''
        ('Sao Paulo', -23.547778)
        ('Mexico City', 19.433333)
        ('Delhi NCR', 28.613889)
        ('Tokyo', 35.689722)
        ('New York-Newark', 40.808611)
        '''

    """
    * methodcaller 创建的函数会在对象上调用参数指定的方法
    """
    s = 'The time has come'
    upcase = methodcaller('upper')
    print(upcase(s))        # THE TIME HAS COME
    hiphenate = methodcaller('replace', ' ', '-')
    print(hiphenate(s))     # The-time-has-come

    """
    * 使用functools.partial冻结参数
    """
    triple = partial(mul, 3)
    print(triple(7))        # 21
    print(list(map(triple, range(1, 10))))      # [3, 6, 9, 12, 15, 18, 21, 24, 27]

    """
    * partial 的第一个参数是一个可调用对象，后面跟着任意个要绑定的定位参数和关键字参数
    """
    nfc = functools.partial(unicodedata.normalize, 'NFC')
    s1 = 'café'
    s2 = 'cafe\u0301'
    print(s1, s2)       # café café
    print(s1 == s2)     # False
    print(nfc(s1) == nfc(s2))       # True



