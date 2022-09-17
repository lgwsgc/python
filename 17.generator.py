"""
通过列表生成式(列表推导式)，我们可以直接创建一个列表。
但是,受到内存限制，列表容量肯定是有限的，而且创建一个包含100万个元素的列表，不仅占用很大的存储空间，而我们仅仅需要访问前几个元素，
那后面绝大多数元素占用的空间都白白浪费了，
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间，在python中，这种一边循环一边计算的机制称为生成器：generator

得到生成器方式：
1.通过列表推导式得到生成器
2.借助函数完成：定义一个以 yield 关键字标识返回值的函数；调用刚刚创建的函数，即可创建一个生成器。
"""
# ----------生成器1------------------
newlist = [x * 3 for x in range(10)]
print(newlist)
# 得到生成器(列表推导式的中括号改成小括号即可)
g = (x * 3 for x in range(10))
print(type(g))  # <class 'generator'>
print(g)  # <generator object <genexpr> at 0x000002C07C8505F0>
# 调用生成器
# 方式1.通过调用__next__()方式得到元素，每次得到一个元素
print(g.__next__())
print(g.__next__())
# 方式2.next(生成器对象(这里是g)) ，该函数是builtins，系统内置函数，每次得到一个元素
print(next(g))
print(next(g))
print(next(g))
# 在next()中，如果生成器元素生成完，继续产生会出现StopIteration错误(生成器一共10个元素，得到10个元素后...)

g1 = (x * 3 for x in range(15))
while True:
    try:
        y = next(g1)
        print(y)
    except StopIteration:
        print('没有更多元素了！')
        break


# ----------生成器2------------------
# 菲波那切数列 Fibonacci sequence
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b
        a, b = b, a + b
        n += 1
    return 'abc'  # 当出现StopIteration时，return的内容会想raise一样抛出


x = fib(8)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

'''
步骤:
1.定义一个函数，函数中使用关键字yield
2.调用函数，接收调用的结果
3.得到的结果就是生成器
4.借助next()或__next__()得到元素

'''


def func():
    n = 0
    while True:
        n += 1
        # print(n)
        yield n  # 类似return n ，yield=return + 暂停


g2 = func()
# print(next(g2))
# print(next(g2))
# print(next(g2))
# print(g2.__next__())
# print(g2.__next__())
# print(g2.__next__())


"""
定义一个以 yield 关键字标识返回值的函数；
调用刚刚创建的函数，即可创建一个生成器。
以下是下面例子的解析:
1) 首先，在创建有 num 生成器的前提下，通过其调用 next() 内置函数，会使 Python 解释器开始执行 intNum() 生成器函数中的代码，
因此会输出“开始执行”，程序会一直执行到yield i，而此时的 i==0，因此 Python 解释器输出“0”。由于受到 yield 的影响，程序会在此处暂停。
2) 然后，我们使用 num 生成器调用 __next__() 方法，该方法的作用和 next() 函数完全相同（事实上，next() 函数的底层执行的也是 __next__()方法，
它会是程序继续执行，即输出“继续执行”，程序又会执行到yield i，此时 i==1，因此输出“1”，然后程序暂停。
3) 最后，我们使用for循环遍历num生成器，之所以能这么做，是因为 for 循环底层会不断地调用 next() 函数，使暂停的程序继续执行，因此会输出后续的结果。
注意，在 Python 2.x 版本中不能使用 __next__() 方法，可以使用 next() 内置函数，另外生成器还有 next() 方法（即以 num.next() 的方式调用）。

除此之外，还可以使用 list() 函数和 tuple() 函数，直接将生成器能生成的所有值存储成列表或者元组的形式
"""


def intNum():
    print("开始执行")
    for i in range(5):
        yield i
        print("继续执行")
    print('执行完成')


num = intNum()
# 调用 next() 内置函数
print(next(num))
# 调用 __next__() 方法
print(num.__next__())
# 通过for循环遍历生成器
for i in num:
    print(i)

# ---------------生成器2-1------------
'''
生成器方法：
1.__next__():获取下一个元素
2.send(value):向每次生成器调用中传值 注意: 第一次调用send(None)
'''


def gen1():
    j = 0
    while j < 5:
        temp = yield j
        print('temp=:', temp)
        for j in range(temp):
            print('----->', j)
        print('*' * 20)
        j += 1
    return '没有更多的内容'


g3 = gen1()
print(g3.send(None))
n1 = g3.send(3)
print("n1:", n1)
n2 = g3.send(4)
print("n2:", n2)
# print(next(g3))
# print(next(g3))
# print(next(g3))
# ---------生成器应用------------------
# 进程 > 线程 > 协程
