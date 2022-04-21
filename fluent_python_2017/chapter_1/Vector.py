from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):                     # __repr__() 自定义输出实例化对象时的信息，一般默认输出的是：<类名 + object + 内存地址>
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)        # hypot() 返回欧几里德范数 sqrt(x*x + y*y)。PS：已知两边 求 第三边 的长度

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)

    def __mul__(self, scalar):              # scalar adj 纯量的; 标量的; 无向量的 / n 数量，标量
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(1, 3)
    v2 = Vector(2, 1)

    v = v1 + v2

    print(v)
    print(abs(v))
    print(v * 3)
    print(abs(v * 3))