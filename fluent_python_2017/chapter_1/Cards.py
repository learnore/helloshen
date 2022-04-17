"""
@author learnore@163.com
@time   2022-04-17 10:52

spades      ♠
diamonds    ♦
clubs       ♣
hearts      ❤
"""
import collections


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
    suits = '♠ ♦ ♣ ❤'.split()

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

    print(deck[0], deck[-1])