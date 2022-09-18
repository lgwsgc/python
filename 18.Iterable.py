# 可迭代的对象： 1.生成器 2.元组 列表 集合 字典 字符串(2中均需要借助iter()函数变成迭代器)
# 如何判断一个对象是否可迭代？
# from collections import Iterable  python==3.6,则不需要加'.abc'
from collections.abc import Iterable

list1 = [1, 2, 3, 4, 5]
f = isinstance(list1, Iterable)
print(f)  # true
f = isinstance('abd', Iterable)
print(f)  # true
f = isinstance(100, Iterable)
print(f)  # false


def func():
    for i in range(6):
        print('i={}'.format(i))
        yield


g = func()
f = isinstance(g, Iterable)
print(f)
'''
迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
迭代器只能往前，不会后退。
[1,2,3,4,5,6,]

可以被next()函数调用并不断返回下一个值的对象成为迭代器: Iterator。

可迭代的 是不是肯定就是 迭代器 ？ 不是
生成器是可迭代的，也是迭代器
列表是可迭代的，但不是迭代器，不过可以通过iter()函数变成迭代器

迭代器 > 生成器
'''
