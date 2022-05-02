### Hello World
* Contributions will show up on my profile.
* And Hello, My name is China Shen.


### 常用库 · 数据类
* [Netlib](http://www.netlib.org)
* [Pandas](http://pandas.pydata.org)
* [Blaze](http://blaze.pydata.org)


### [Python 之禅](https://www.python.org/doc/humor/#the-zen-of-python)
* “实用胜于纯粹。”
* “不能让特例特殊到开始破坏既定规则。”

### “快速失败”哲学
* 当字典 d[k] 不能找到正确的键的时候，Python 会抛出异常
* dict.get 并不是处理找不到的键的最好方法

### [Python Tutor](https://pythontutor.com/)
* 是一个对 Python 运行原理进行可视化分析的工具
![Python Tutor](https://github.com/learnore/helloshen/blob/main/fluent_python_2017/image/python_tutor.png "Python Tutor")

### [排序集合模块](https://code.activestate.com/recipes/577197-sortedcollection/)
* Python 的高产贡献者 Raymond Hettinger 写了一个排序集合模块
* 模块里集成了 bisect 功能，但是比独立的 bisect 更易用


### 实用的一些 🔗
[Python 语言参考手册里的“Data Model”一章](https://docs.python.org/3/reference/datamodel.html)
* 是最符合规范的知识来源

[维基百科 - 对象模型](http://en.wikipedia.org/wiki/Object_model)  

[Python 数据模型](https://docs.python.org/3/reference/datamodel.html)  

[memoryview 内存视图](https://stackoverflow.com/questions/4845418/when-should-a-memoryview-be-used/)
* 内存视图其实是泛化和去数学化的 NumPy 数组。它让你在不需要复制内容的前提下，在数据结构之间共享内存。
* 其中数据结构可以是任何形式，比如 PIL 图片、SQLite 数据库和 NumPy 的数组，等等。
* 这个功能在处理大型数据集合的时候非常重要。


Alex Martelli 的《Python 技术手册（第 2 版）》对数据模型的讲解很精彩。 Martelli 对属性访问机制的描述，
应该是除了 CPython 中的 C 源码之外在这方面最权威的解释。Martelli 还是 Stack Overflow 上的高产贡献者，
在他名下差不多有 5000 条答案，你也可以去他的 [Stack Overflow 主页](http://stackoverflow.com/users/95810/alex-martelli) 上看看。

[“Sorting HOW TO”](https://docs.python.org/3/howto/sorting.html)
* Python 官方网站，通过几个例子讲解了 sorted 和 list.sort 的高级用法。

[Python 词汇表](https://docs.python.org/3/glossary.html#term-hashable)

[“Built-in Types”](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

[“PEP 3132 — Extended Iterable Unpacking”](https://www.python.org/dev/peps/pep-3132/)
* 算得上是使用 *extra 句法进行平行赋值的权威指南

### 引言的乐趣
>> Tim Peters
传奇的核心开发者，“Python 之禅”作者
> 
> 要不这样吧，如果编程语言里有个地方你弄不明白，而正好又有个人用了这个功能，
那就开枪把他打死。这比学习新特性要容易些，然后过不了多久，那些活下来的程
序员就会开始用 0.9.6 版的 Python，而且他们只需要使用这个版本中易于理解的那一
小部分就好了（眨眼）。


>> Jim Hugunin
Jython 的作者，AspectJ 的作者之一，.NET DLR 架构师
> 
> Guido 对语言设计美学的深入理解让人震惊。我认识不少很不错的编程语言设计者，
他们设计出来的东西确实很精彩，但是从来都不会有用户。Guido 知道如何在理论
上做出一定妥协，设计出来的语言让使用者觉得如沐春风，这真是不可多得。


>> Geurts、Meertens 和 Pemberton
ABC Programmer’s Handbook
> 
> 你可能注意到了，之前提到的几个操作可以无差别地应用于文本、列表和表格上。
我们把文本、列表和表格叫作数据火车……FOR 命令通常能作用于数据火车上。


>> A. M. Kuchling
《代码之美》第 18 章“Python 的字典类：如何打造全能战士”
> 
> 字典 dict 这个数据结构活跃在所有 Python 程序的背后，即便你的源码里并没有直接用到它。