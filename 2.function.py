"""
函数总结:
def func(**kwargs):
    pass
调用函数时   func(**kwargs)表示拆包
定义函数时   def func(**kwargs):表示装包

"""
# 函数，打印每位同学的名字和年龄
students = {'001': ('蔡徐坤', 20), '002': ('王源', 22), '003': ('易烊千玺', 19), '004': ('王俊凯', 19)}


def print_boy(name, **persons):
    print("{}喜欢的明星是：".format(name))
    if isinstance(persons, dict):
        keys = persons.keys()
        values = persons.values()
        # print(keys)
        # print(values)
        for name, age in values:
            print("{}的年龄是:{}".format(name, age))


# 调用
print_boy('weiwei', **students)



