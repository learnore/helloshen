# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_slice
  Description : seq[start:stop:step]

                切片：在 Python 里，像列表（list）、元组（tuple）和字符串（str）这类序列类型都支持切片
                操作，但是实际上切片操作比人们所想象的要强大很多。
  Author      : chenyushencc@gmail.com
  date        : 2022/4/25 7:38
-------------------------------------------------
"""


if __name__ == '__main__':
    """
    一个众所周知的秘密是，我们还可以用 s[a:b:c] 的形式对 s 在 a 和 b 之间以 c 为间隔取值。c 的值还可以为负，负值意味着反向取值
    """
    s = 'bicycle'
    print(s[::3])
    print(s[::-1])
    print(s[::-2])

    invoice = """
0.....6...................................40........52...55........
1909  Pimoroni PiBrella                   $17.50    3    $52.50
1489  6mm Tactile Switch x20              $4.95     2    $9.90
1510  Panavise Jr. - PV-201               $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240              $34.95    1    $34.95
    """
    SKU = slice(0, 6)
    DESCRIPTION = slice(6, 40)
    UNIT_PRICE = slice(40, 52)
    QUANTITY = slice(52, 55)
    ITEM_TOTAL = slice(55, None)
    for item in invoice.split('\n')[2:]:
        print(item[SKU], item[DESCRIPTION], item[UNIT_PRICE], item[QUANTITY], item[ITEM_TOTAL])

    print("------------------------------------------------------------------------")
    l = list(range(10))
    print(l)
    l[2:5] = [20, 30]
    print(l)
    del l[5:7]
    print(l)
    l[3::2] = [11, 22]
    print(l)
    """
    * tips: 如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代对象。即便只有单独一个值，也要把它转换成可迭代的序列
    """
    l[2:5] = [100]  # l[2:5] = 100  TypeError: can only assign an iterable
    print(l)

    print("------------------------------------------------------------------------")
    m = [1, 2, 3]
    print(m * 5)
    print('abcd ' * 3)

    """
    * tips：初始化不可以使用 [[] * 3 for i in range(3)]
    *       因为三个引用都指向的都是同一个列表，不是我们所想要的结果
    """
    board = [['_'] * 3 for i in range(3)]
    print(board)
    board[1][2] = 'O'
    print(board)

    """
    * X 示范 X
    """
    weird_board = [['_'] * 3] * 3
    print(weird_board)          # 看起来没问题，但是接下来赋值就会出错
    weird_board[1][2] = 'X'
    print(weird_board)          # [['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]

    """
    * X 示范 X == 以下 for 循环的代码
    * 追加同一个行对象（row）3 次到游戏板（board）
    """
    row = ['_'] * 3
    board = []
    for i in range(3):
        board.append(row)
    board[1][2] = 'X'
    print(board)

    """
    * √ 示范 √
    * 每次迭代中都新建了一个列表，作为新的一行（row）追加到游戏板（board）
    """
    board = []
    for i in range(3):
        row = ['_'] * 3
        board.append(row)
    board[1][2] = 'O'
    print(board)
