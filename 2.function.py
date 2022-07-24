
# 函数，打印每位同学的名字和年龄
students = {'001': ('蔡徐坤', 20), '002': ('王源', 22), '003': ('易烊千玺', 19), '004': ('王俊凯', 19)}


def print_boy(name, persons):
    if isinstance(persons, dict):
        keys = persons.keys()
        values = persons.values()
        print(keys)
        print(values)
        # for i in keys:
        for name, age in values:
            print("{}的年龄是:{}".format(name, age))


# 调用
# print_boy('李岗威', students)
def func(**kwargs):  # key word argument
    print(kwargs)


func(a=1, b=2, c=3)
