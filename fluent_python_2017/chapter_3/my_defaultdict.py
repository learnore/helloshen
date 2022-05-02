# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : my_defaultdict      -->     __missing__(self, key) 的引用
  Description : 处理找不到的键的一个选择
                比如，我们新建了这样一个字典：dd = defaultdict(list)，如果键 'new-key' 在 dd 中还
                不存在的话，表达式 dd['new-key'] 会按照以下的步骤来行事。
                (1) 调用 list() 来建立一个新列表。
                (2) 把这个新列表作为值，'new-key' 作为它的键，放到 dd 中。
                (3) 返回这个列表的引用。

                字典的变种：
                collections.OrderedDict
                    这个类型在添加键的时候会保持顺序，因此键的迭代次序总是一致的。OrderedDict
                    的 popitem 方法默认删除并返回的是字典里的最后一个元素，但是如果像 my_odict.
                    popitem(last=False) 这样调用它，那么它删除并返回第一个被添加进去的元素。

                collections.ChainMap
                    该类型可以容纳数个不同的映射对象，然后在进行键查找操作的时候，这些对象会被当
                    作一个整体被逐个查找，直到键被找到为止。这个功能在给有嵌套作用域的语言做解
                    释器的时候很有用，可以用一个映射对象来代表一个作用域的上下文。在 collections
                    文档介绍 ChainMap 对象的那一部分（https://docs.python.org/3/library/collections.html#
                    collections.ChainMap）里有一些具体的使用示例，其中包含了下面这个 Python 变量查
                    询规则的代码片段：

                    import builtins
                    pylookup = ChainMap(locals(), globals(), vars(builtins))

                collections.Counter
                    这个映射类型会给键准备一个整数计数器。每次更新一个键的时候都会增加这个计数
                    器。所以这个类型可以用来给可散列表对象计数，或者是当成多重集来用——多重集合
                    就是集合里的元素可以出现不止一次。Counter 实现了 + 和 - 运算符用来合并记录，还
                    有像 most_common([n]) 这类很有用的方法。most_common([n]) 会按照次序返回映射里最
                    常见的 n 个键和它们的计数，详情参阅文档（https://docs.python.org/3/library/collections.
                    html#collections.Counter）。下面的小例子利用 Counter 来计算单词中各个字母出现的次数：

                    >>> ct = collections.Counter('abracadabra')
                    >>> ct
                    Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
                    >>> ct.update('aaaaazzz')
                    >>> ct
                    Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
                    >>> ct.most_common(2)
                    [('a', 10), ('z', 3)]

                colllections.UserDict
                    这个类其实就是把标准 dict 用纯 Python 又实现了一遍。

  Author      : chenyushencc@gmail.com
  date        : 2022/5/2 21:22
-------------------------------------------------
"""
import re
import sys
import collections


class StrKeyDict0(dict):                # StrKeyDict0 继承了 dict

    def __missing__(self, key):
        if isinstance(key, str):        # 如果找不到的键本身就是字符串，那就抛出 KeyError 异常
            raise KeyError(key)

        return self[str(key)]           # 如果找不到的键不是字符串，那么把它转换成字符串再进行查找

    def get(self, key, default=None):
        try:
            return self[key]            # get 方法把查找工作用 self[key] 的形式委托给 __getitem__，这样在宣布查找失败之前，还能通过 __missing__ 再给某个键一个机会
        except KeyError:
            return default              # 如果抛出 KeyError，那么说明 __missing__ 也失败了，于是返回 default

    def __contains__(self, key):
        """
        * 先按照传入键的原本的值来查找（我们的映射类型中可能含有非字符串的键），如果没
        * 找到，再用 str() 方法把键转换成字符串再查找一次
        """
        return key in self.keys() or str(key) in self.keys()


class StrKeyDict(collections.UserDict):         # StrKeyDict 是对 UserDict 的扩展
    """
    * 因为 UserDict 继承的是 MutableMapping，所以 StrKeyDict 里剩下的那些映射类型的方法
    * 都是从 UserDict、MutableMapping 和 Mapping 这些超类继承而来的。特别是最后的 Mapping
    * 类，它虽然是一个抽象基类（ABC），但它却提供了好几个实用的方法。
    """

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)

        return self[str(key)]

    def __contains__(self, key):
        """
        * __contains__ 则更简洁些。这里可以放心假设所有已经存储的键都是字符串。因此，只
        * 要在 self.data 上查询就好了，并不需要像 StrKeyDict0 那样去麻烦 self.keys()。
        """
        return str(key) in self.data

    def __setitem__(self, key, value):
        """
        * __setitem__ 会把所有的键都转换成字符串。由于把具体的实现委托给了 self.data 属性
        """
        self.data[str(key)] = value


if __name__ == '__main__':
    """
    * 创建一个从单词到其出现情况的映射
    """
    WORD_RE = re.compile(r'\w+')

    """
    * 把 list 构造方法作为 default_factory 来创建一个 defaultdict
    * 如果在创建 defaultdict 的时候没有指定 default_factory，查询不存在的键会触发 KeyError
    * defaultdict 里的 default_factory 只会在 __getitem__ 里被调用，在其他的方法里完全不会发挥作用
    * 所有这一切背后的功臣其实是特殊方法 __missing__，它会在 defaultdict 遇到找不到的键的时候调用 default_factory
    * __missing__ 方法只会被 __getitem__ 调用（比如在表达式 d[k] 中）
    """
    index = collections.defaultdict(list)
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            word = re.match.group()
            column_no = re.match.start() + 1
            location = (line_no, column_no)
            """
            * 如果 index 并没有 word 的记录，那么 default_factory 会被调用，为查询不到的键创造
            * 一个值。这个值在这里是一个空的列表，然后这个空列表被赋值给 index[word]，继而
            * 被当作返回值返回，因此 .append(location) 操作总能成功
            """
            index[word].append(location)

    for word in sorted(index, key=str.upper()):
        print(word, index[word])