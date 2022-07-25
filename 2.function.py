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
# print_boy('weiwei', **students)
"""
打印某人学过那些课程
courses = ['html','mysql','python']

"""


def study_course(name, *args):
    if len(args) > 0:
        for i in args:
            print("{}学过{}".format(name, i))
    else:
        print("未学过编程知识")


courses = ['html', 'mysql', 'python']
study_course("lgw", *courses)
"""
0.无参函数：
格式：
def func():
    pass
调用：
func()
1.有参函数：
    1.普通参数：
    格式：
    def func(name, age): 形参
        pass
    调用：
    func(name, age) ---->实参  形参要与实参个数保持一致
    2.可变参数：
    格式1：
    def func(*args)
        pass
    调用：
    func() --->调用时，实参可以是多个，也可以没有 *不能是关键字参数
    eg： func(3) , func(2,"h")
    格式2：
    def func(**kwargs)
        pass
    调用：
    func() --->调用时，实参可以是多个，也可以没有 **必须是关键字参数
    格式3：
    def func(*args, **kwargs)
        pass
    
    list=[1,2,3,4]
    dict={'a':1,'b':2,'c':3,}
    调用：
    func(*args,**kwargs) #func(1,2,3,4,'a':1,'b':2,'c':3,)拆包
    格式4：
    def func(name, *args, **kwargs): # 必须有
        pass
    
    调用：
    func('tom') 
2.默认值+关键字函数：
格式：
def func(name, age=18)：
    pass
调用：
func('tom') # 有默认值的可写可不写，写了会覆盖掉默认值，不写使用默认值
"""


def func(*args, **kwargs):
    print(list1)
    print(dict1)


list1 = [1, 2, 3, 4]
dict1 = {'a': "apple", 'b': "banana", 'c': "cat", }
func(list1, dict1)
