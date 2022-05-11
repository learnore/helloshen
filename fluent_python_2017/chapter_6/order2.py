# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : order2
  Description : 比 order1 更见简洁，少了 12 行代码
  Author      : chenyushencc@gmail.com
  date        : 2022/5/11 8:23
-------------------------------------------------
"""
import inspect
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    """
    * 上下文
    *     把一些计算委托给实现不同算法的可互换组件，它提供服务。在这个电商示例中，上下文是 Order，它会根据不同的算法计算促销折扣。
    """

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)

        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)     # 计算折扣只需调用 self.promotion() 函数

        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# 没有抽象类
def fidelity_promo(order):          # 各个策略都是函数
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1

    return discount


def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07

    return 0


def best_promo(order):
    """选择可用的最佳折扣"""
    """
    * 注意：
    * 
    * 虽然示例 6-6 可用，而且易于阅读，但是有些重复可能会导致不易察觉的缺陷：若想添加
    * 新的促销策略，要定义相应的函数，还要记得把它添加到 promos 列表中；否则，当新促销
    * 函数显式地作为参数传给 Order 时，它是可用的，但是 best_promo 不会考虑它。
    * 
    * 解决方法：见本脚本 globals_best_promo() 或 inspect_best_promo() 方法
    """
    promos = [fidelity_promo, bulk_item_promo, large_order_promo]

    return max(promo(order) for promo in promos)


def globals_best_promo(order):
    """找出所有的促销策略"""
    """
    * globals()
    *   返回一个字典，表示当前的全局符号表。这个符号表始终针对当前模块（对函数或方法
    *   来说，是指定义它们的模块，而不是调用它们的模块）。
    """
    promos = [globals()[name] for name in globals()     # 迭代 globals() 返回字典中的各个 name
              if name.endswith('_promo')                # 只选择以 _promo 结尾的名称
              and name != 'best_promo']                 # 过滤掉 best_promo 自身，防止无限递归

    return max(promo(order) for promo in promos)


def inspect_best_promo(order):
    """找出所有的促销策略"""
    """内省单独的 promotions 模块，构建 promos 列表"""
    """要导入 promotions 模块，以及提供高阶内省函数的 inspect 模块"""
    promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]

    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    print(Order(joe, cart, fidelity_promo))
    print(Order(ann, cart, fidelity_promo))

    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]
    print(Order(joe, banana_cart, bulk_item_promo))

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print(Order(joe, long_order, large_order_promo))
    print(Order(joe, cart, large_order_promo))

    """
    * best_promo 函数计算所有折扣，并返回额度最大的
    """
    print(Order(joe, long_order, best_promo))
    print(Order(joe, banana_cart, best_promo))
    print(Order(ann, cart, best_promo))