# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  IDE         : PyCharm
  File Name   : keyword_only_args
  Description : 从定位参数到仅限关键字参数
  Author      : chenyushencc@gmail.com
  date        : 2022/5/6 8:19
-------------------------------------------------
"""


def tag(name, *content, cls=None, **attrs):
    """生成一个或多个 HTML 标签"""
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
    print(tag('br'))                                    # <br />
    print(tag('p', 'hello'))                            # <p>hello</p>
    print(tag('p', 'hello', 'world'))
    print(tag('p', 'hello', id=33))                     # <p id="33">hello</p>
    print(tag('p', 'hello', 'world', cls='sidebar'))    # <p class="sidebar">hello</p>      <p class="sidebar">world</p>
    print(tag(content='testing', name='img'))           # <img content="testing" />
    my_tag = {
        'name': 'img',
        'title': 'Sunset Boulevard',
        'src': 'sunset.images',
        'cls': 'framed'
    }
    print(tag(**my_tag))        # <img class="framed" src="sunset.images" title="Sunset Boulevard" />
