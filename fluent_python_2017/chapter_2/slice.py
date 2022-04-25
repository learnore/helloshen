# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : slice
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
