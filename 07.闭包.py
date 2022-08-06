"""
嵌套：

闭包：(在装饰器里用)由函数及相关的引用环境组合而成的实体
    1.嵌套函数
    2.内部函数引用了外部函数的变量
    3.返回值是内部函数
"""

# 嵌套


def outer():
    a = 100

    def inner():
        b = 200
        # b += a # 内部函数可以使用外部变量
        nonlocal a  # 若想修改，需要在内部函数中添加：nonlocal
        a += b  # 内部函数不可直接修改外部变量
        print('我是内部函数', a)

    # result = locals()  # locals()表示查看函数中的局部变量,以字典的形式返回
    # print(result)
    print(a)
    inner()


# outer()


# 闭包
def outer1(n):
    a = 10

    def inner():
        b = a + n
        print('我是内部函数', b)

    return inner


r = outer1(3)
print(r)  # r是inner的地址
