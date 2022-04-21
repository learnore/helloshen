# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : test
  Description : 向量类
  Author      : chenyushencc@gmail.com
  date        : 2022/04/17 10:52
-------------------------------------------------
"""
import collections
from random import choice


"""
tips
namedtuple 用于快速构建有（较少）属性且无方法的类
"""
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    构建一副扑克牌
    """
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades hearts diamonds clubs'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


if __name__ == '__main__':
    # beer_card = Card('7', '❤')
    # print(beer_card)

    deck = FrenchDeck()
    # print(len(deck))

    # print(deck[0], deck[-1])

    # print(choice(deck))     # 随机抽牌
    # print(choice(deck))     # 随机抽牌

    # for card in reversed(deck):
    #     print(card)

    """
    给扑克的每个花色赋予值：
    最大  spades      ♠
    其次  hearts      ❤
    次之  diamonds    ♦
    最小  clubs       ♣
    """
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    for card in sorted(deck, key=spades_high):  # 输出排好序的扑克
        print(card)
