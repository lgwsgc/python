"""
装饰器:
     遵循开放封闭原则，在不改变原函数的情况下，拓展了函数的功能
功能: 1.引入日志
     2.函数执行时间统计
     3.执行函数前预备处理
     4.执行函数后清理功能
     5.权限校验等场景
     6.缓存

"""


# 定义装饰器


def decorate(func):
    def warpper():
        func()
        print('刷漆')
        print('铺地板')
        print('买家电')

    return warpper


@decorate  # 等价house = decorate(house)
def house():
    print('毛坯房')


# house()
"""
带参数的装饰器
"""


def decorate1(func):
    def warpper1(*args, **kwargs):  # 原函数含参，则装饰器内部函数也含参
        # args是一个元组
        func(*args, **kwargs)  # 拆包
        print('刷漆')
        print('铺地板')
        print('买家电')

    return warpper1


@decorate1  # 等价house = decorate(house)
def house1(address):
    print('毛坯房的地址{}'.format(address))


@decorate1
def cangku(address, area):
    print('房子地址在：{}，是一个毛坯房，建筑面积是：{}平米'.format(address, area))


@decorate1
def bieshu(address, area, price):
    print('房子地址在：{}，是一个毛坯房，建筑面积是：{}平米,价值{}万元'.format(address, area, price))


@decorate1
def hotel(address, area, price):
    print('酒店地址在：{}，是一个毛坯房，建筑面积是：{}平米,价值{}万元'.format(address, area, price))


hotel('梦想之家', 10000, price=1000)
print('-' * 36)
bieshu('梦想之家', 10000, 1000)
print('-' * 36)
cangku('天上人间', 1000)
print('-' * 36)
house1('北京四合院')
"""
含返回值的装饰器:原函数有返回值，装饰器内部函数也要有返回值
"""


def decorate2(func):
    def warpper2(*args, **kwargs):
        r = func(*args, **kwargs)
        print('是一个毛坯房'.format(r))
        print('刷漆')
        print('铺地板')
        print('买家电')
        return 60000

    return warpper2


@decorate2
def house2():
    print('毛坯房的地址{}')
    return 50000


r = house2()
print(r)
