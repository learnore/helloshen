# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : touple
  Description : 元组
  Author      : chenyushencc@gmail.com
  date        : 2022/4/23 22:16
-------------------------------------------------
"""

if __name__ == "__main__":
    lax_coordinates = (33.9425, -118.408056)
    print(lax_coordinates)
    latitude, longitude = lax_coordinates  # 元组拆包
    print(latitude)
    """
    一个很优雅的写法：不使用中间变量，交换两个变量的值
    """
    latitude, longitude = longitude, latitude
    print(latitude)

    print("-------------------------------------------------------------")
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
    print(city, year, pop, chg, area)
    print(city)
    print(year)
    print(pop)
    print(chg)
    print(area)

    print("-------------------------------------------------------------")
    traveler_ids = [('USA', '31195855', 1), ('BRA', 'CE342567', 2), ('ESP', 'XDA205856', 3)]
    """
    元组拆包之一
    """
    for passport in sorted(traveler_ids):
        print('%s/%s - %d' % passport)
    """
    元组拆包之二，使用 _ 占位符
    """
    for country, _, _ in traveler_ids:
        print(country)
    """
    * tips 元组拆包之三，使用 * 来处理多余的元素，将用数组 [] 表示，可以表示 0 到无数个（0 是空数组）
    """
    for country, *data in traveler_ids:
        print(country)
        print(data)
    for *data, number in traveler_ids:
        print(data)
        print(number)
    for country, *data, number in traveler_ids:
        print(country)
        print(data)
        print(number)
    for country, people, *data, number in traveler_ids:
        print(country)
        print(people)
        print(data)
        print(number)

    print("-------------------------------------------------------------")
    """
    * 还可以用 * 运算符把一个可迭代对象拆开作为函数的参数
    """
    print(divmod(20, 8))
    t = (20, 8)
    print(divmod(*t))       # 同 divmod(20, 8)，思考：为啥不是 divmod(t) ?
    a, b = 20, 8
    print(divmod(a, b))     # 因为 t 是代表的多个元素
    quotient, remainder = divmod(*t)
    print(quotient, remainder)

    print("-------------------------------------------------------------")
    import os
    """
    * os.path.split() 函数就会返回以路径和最后一个文件名组成的元组 (path, last_part)
    """
    _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
    print(filename)

    print("-------------------------------------------------------------")
    print("*** 字符串格式化 format 参考博客：https://www.cnblogs.com/Alliswell-WP/p/Python3_format.html ***")
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))      # ^、<、>分别是居中、左对齐、右对齐
    fmt = '{:>15} | {:>9.4f} | {:>9.4f}'
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude <= 0:
            print(fmt.format(name, latitude, longitude))

    print("-------------------------------------------------------------")
    print("-----------------collections.namedtuple----------------------")
    from collections import namedtuple
    # namedtuple 创建的方式一：可以是由数个字符串组成的可迭代对象
    City = namedtuple('City', 'name country population coordinates')
    # namedtuple 创建的方式二：由空格分隔开的字段名组成的字符串
    # City = namedtuple('City', ['name', 'country', 'population', 'coordinates'])
    tokyo = City('Tokyo', 'JP', '36.333', (35.689722, 139.691667))
    print(tokyo)
    print(tokyo.population)
    print(tokyo.coordinates)
    print(tokyo[1])         # 可以通过字段名或者位置来获取一个字段的信息
    print(City._fields)     # _fields 属性是一个包含这个类所有字段名称的元组

    LatLong = namedtuple('LatLong', 'lat long')
    delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    delhi = City._make(delhi_data)  # _make() 同 City(*delhi_data) 通过接受一个可迭代对象来生成这个类的一个实例
    print(delhi._asdict())          # _asdict 把具名元组以 collections.OrderedDict 的形式返回，以字典形式返回
