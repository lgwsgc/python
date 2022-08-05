"""
global 变量的范围
局部变量 :声明在函数内部的变量，不能在函数外使用，否则会报错
全局变量 :若需修改且全局变量不可变，通常声明在函数内部的开头：global 变量名；不修改则不需要
局部和全局尽量不要使用相同的变量名，否则会报错

可变和不可变：
可变：地址不变，内容改变 list dict set
不可变：只要内容改变，地址就改变 int str float tuple frozenset
"""
name = '蕾姆'
list1 = [1, 2, 3, 4, 5, 6]


def func():
    # 函数内部声明的变量，局部变量
    name = '妲己'
    print(name)
    print(list1)


def func1():
    global name
    print(name)
    name += "在思念主人"
    list1.append(8)
    print(name)
    print(list1)


def func2():
    pass


func()
func1()
