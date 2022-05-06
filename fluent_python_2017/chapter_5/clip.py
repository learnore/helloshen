# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : clip
  Description : 在指定长度附近截断字符串的函数
  Author      : chenyushencc@gmail.com
  date        : 2022/5/6 22:05
-------------------------------------------------
"""
from inspect import signature


def clip(text, max_len=80):
    """
    * 在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)

        if space_after >= 0:
            end = space_after
    if end is None:
        end = len(text)

    return text[:end].rstrip()


def clip_annotations(text:str, max_len:'int > 0'=80) -> str:        # 有注解的函数声明
    """
    * 在max_len前面或后面的第一个空格处截断文本
    * 注解不会做任何处理，只是存储在函数的 __annotations__ 属性（一个字典）中
    *
    * Python 对注解所做的唯一的事情是，把它们存储在函数的 __annotations__ 属性里。仅
    * 此而已，Python 不做检查、不做强制、不做验证，什么操作都不做。换句话说，注解对
    * Python 解释器没有任何意义。注解只是元数据，可以供 IDE、框架和装饰器等工具使用。
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
    if space_before >= 0:
        end = space_before
    else:
        space_after = text.rfind(' ', max_len)
    if space_after >= 0:
        end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()


if __name__ == '__main__':
    print(clip.__defaults__)                # (80,)
    print(clip.__code__)
    print(clip.__code__.co_varnames)        # ('text', 'max_len', 'end', 'space_before', 'space_after')
    print(clip.__code__.co_argcount)        # 2

    sig = signature(clip)
    print(sig)
    print(str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)

    print(clip_annotations.__annotations__)     # {'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}
    sig_annotations = signature(clip_annotations)
    print(sig_annotations.return_annotation)
    for param in sig_annotations.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ':', param.name, '=', param.default)
        # <class 'str'> : text = <class 'inspect._empty'>
        # 'int > 0'     : max_len = 80

