# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : decorate_order
  Description : promos 列表中的值使用 promotion 装饰器填充
  Author      : chenyushencc@gmail.com
  date        : 2022/5/29 11:53
-------------------------------------------------
"""
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


promos = []


def promotion(promo_func):      # promotion 把 promo_func 添加到 promos 列表中，然后原封不动地将其返回。
    promos.append(promo_func)
    return promo_func


@promotion      # 被 @promotion 装饰的函数都会添加到 promos 列表中。
def fidelity(order):
    """ 为积分为1000或以上的顾客提供5%折扣 """
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion      # 被 @promotion 装饰的函数都会添加到 promos 列表中。
def bulk_item(order):
    """ 单个商品为20个或以上时提供10%折扣 """
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1

    return discount


@promotion      # 被 @promotion 装饰的函数都会添加到 promos 列表中。
def large_order(order):
    """ 订单中的不同商品达到10个或以上时提供7%折扣 """
    discount_items = {item.product for item in order.cart}
    if len(discount_items) >= 10:
        return order.total() * .07

    return 0


def best_promo(order):      # best_promos 无需修改，因为它依赖 promos 列表。
    """ 选择可用的最佳折扣 """
    return max(promo(order) for promo in promos)


if __name__ == "__main__":
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    print(Order(joe, cart, fidelity))
    print(Order(ann, cart, fidelity))

    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apple', 10, 1.5)]
    print(Order(joe, banana_cart, bulk_item))

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print(Order(joe, long_order, large_order))
    print(Order(joe, cart, large_order))

    """
    * best_promo 函数计算所有折扣，并返回额度最大的
    """
    print(Order(joe, long_order, best_promo))
    print(Order(joe, banana_cart, best_promo))
    print(Order(ann, cart, best_promo))