"""
匿名函数:用lambda关键字,可接收多个参数，但只能返回一个返回值
格式:
    lambda 参数列表: 运算表达式
"""
from functools import reduce


def text(a):
    return a + 1


result = text(4)
print(result)
r = lambda a: a + 1
res = r(4)
print(res)

s = lambda x, y, z: x + y + z
answer = s(1, 2, 3)
print(answer)
"""
使用场景:作为参数使用
"""


def add(a, f):
    print('----->', a)
    r = f(a)
    print('====>', r)


add(2, lambda x: x ** 2)
"""
高阶函数:一个函数的参数是另一个函数
系统高阶:max，min，sorted，filter，map(映射),reduce
"""
m = max(4, 7)
print(m)

n = max([2, 4, 1, 6, 9, 7])
print(n)
list1 = [('rose', 18), ('jack', 17), ('tom', 20), ('tony', 21), ('lily', 19)]
Max = max(list1, key=lambda x: x[1])
print(Max)
Min = min(list1, key=lambda x: x[1])
print(Min)
max_Age = sorted(list1, key=lambda x: x[1])  # 从小到大
print(max_Age)
min_Age = sorted(list1, key=lambda x: x[1], reverse=True)  # 从大到小
print(min_Age)

guolv = filter(lambda x: x[1] > 19, list1)  # 过滤器，filter的匿名函数要求返回值必须是Boolean类型，且Boolean条件才符合过滤条件
print(list(guolv))  # 通过列表强转成列表

ma = map(lambda x: x[1], list1)  # 通过匿名函数指明提取内容，并对内容进行加工
mb = map(lambda x: x[0].title(), list1)
print(list(ma))
print(list(mb))  # 首字母大写

r = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(r)

# zip()
