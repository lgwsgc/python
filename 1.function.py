"""
1.关键字def 2.函数体有缩进 3.函数名()
快捷鍵：
自動格式化：ctrl+alt+l
快速提示：alt+enter/alt+shift+enter
"""
"""
1.无参数
格式：def 函数名():
        函数体
"""
# 定义函数：随机数的生成
import random


def generate_random():
    for i in range(10):
        ran = random.randint(1, 20)
        print(ran)


# 打印該函數內存地址
print(generate_random)
# 調用:函數名()
generate_random()
print('-' * 40)
"""
2.有参数
格式：def 函數名(参数，参数，..):
        函数体
调用：
    pass
"""


# 求随机数的函数，产生个数待定？？？
def generate_random1(num):  # 形参
    for i in range(num):
        ran = random.randint(1, 10)
        print(ran)


generate_random1(3)  # 实参


# 加法函数
def add(a, b):  # 几个形参对应几个实参
    result = a + b
    print("和:", result)


# 调用
add(3, 6)
"""
定义一个登录函数，参数是: uname，pwd
函数体：
判断参数传过来的uname，password是否正确，如果正确则登陆成功，否则打印登录失败
"""


def login(username, password):
    uname = "admin123"
    pwd = '112233'
    for i in range(3):
        if username == uname and password == pwd:
            print("登陆成功")
            break
        else:
            print("登录失败")
            username = input("请输入用户名:")
            password = input("请输入密码:")
    else:
        print("账户锁定")


# username = input("请输入用户名:")
# password = input("请输入密码:")
# login(username, password)


# 找出最大值
def max(iterable):
    max = iterable[0]
    for i in iterable:
        if i > max:
            max = i
    print("max=", max)


# 找出最大值
def min(iterable):
    min = iterable[0]
    for i in iterable:
        if i < min:
            min = i
    print("min:", min)


list_1 = [1, 3, -2, 2, 6, 4, 76]
list_1.sort()
max(list_1)
min(list_1)
tuple1 = (1, 4, -1, 2, 6, 8, 3)
max(tuple1)
min(tuple1)
# sort 排序 min 最小值 reverse排序
# 判断是什么类型:isinstance(变量，类型关键字)


def is_list(x):
    x = int(isinstance(x, list))
    if x == 1:
        print("可以排序和翻转")
    else:
        print("不可以排序和翻转")


x = (1, 2, 3)
is_list(x)