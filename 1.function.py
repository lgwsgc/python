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
"""
集合：无序不重复的序列
    list tuple --->set()  
"""
s = {1, 2, 4, 2, 7, 0, 4}
for i in s:
    print(i)
"""
内置函数：
    添加：add update
    删除：remove discard pop clear
运算相关：
    - difference()差集
    | union()并集
    & intersection() 交集
    ^ symmetric_difference() 异或
可变和不可变：
可变：地址不变，内容改变 list dict set
不可变：只要内容改变，地址就改变 int str float tuple frozenset
x=[1,2,3]
x1 = x
x = [1,2,3,4]
print(x1) 输出结果x1=[1,2,3,4],原因，列表是可变的
y = "asd"
y1 = y
y = "asdf"
print(y1) 输出结果y1="asd",原因，字符串是不可变的

类型转换：
str--->list set ...
list--->set tuple dict... 

函数：增加代码的复用性，减少代码冗余
"""

"""
可变参数
定义方式：
    def add(name，age，*args)
        pass
注意，可变参数放在后面，不变参数放在前面
可变参数+关键字参数
定义方式：
    def add(a，b=10): #b=10是默认值，调用时可以传一个参数，也可以是两个，两个的话会覆盖掉默认值
        pass                如果是3个以上也可以，传入参数是一次覆盖，可以使用关键字指定覆盖
"""


# 一颗*代表元组，两颗*代表字典
def add_sum(*args):  # args = arguments
    sum = 0
    if len(args) > 0:
        for i in args:
            sum += i
        print("sum = ", sum)
    else:
        print("无元素可加")


add_sum(1, 2, 3, 4)

add_sum(1, 3, 6)
