from collections import Counter

"""
1、{}.get('key') 获取对象对应的 value
"""
# 例：统计词频
# 方法 I
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
result = {}
for color in colors:
    if result.get(color) is None:  # 1、{}.get('key') 获取对象对应的 value
        result[color] = 1
    else:
        result[color] += 1
print(result)       # {'red': 2, 'blue': 3, 'green': 1}


# 方法 II - Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
c = Counter(colors)
print(c)        # Counter({'blue': 3, 'red': 2, 'green': 1})
print(dict(c))  # {'red': 2, 'blue': 3, 'green': 1}
print(c.elements())         # <itertools.chain object at 0x000001B605D1BFD0>    存的地址
print(list(c.elements()))   # ['red', 'red', 'blue', 'blue', 'blue', 'green']
