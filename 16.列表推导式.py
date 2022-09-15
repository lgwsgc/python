# 列表推导式(除了列表，还有字典，集合)
# 旧列表--> 新列表

# 1.列表推导式:  格式: [表达式 for 变量 in 旧列表] 或者 [表达式 for 变量 in 旧列表 if 条件]

# 过滤掉长度小于等于3的人名
names = ['tom', 'lily', 'maria', 'lihua', 'ma', 'ding']
# new_names = []
result = [name for name in names if len(name) >= 4]
print(result)
result = [name.capitalize() for name in names if len(name) >= 4]
print(result)

"""
列表表达式等价于这个函数
def func(names):
    new_list = []
    for name in names:
        if len(name) >= 4:
            name = name.capitalize()//首字母大写
            new_list.append(name)
    return new_list

# 调用
x = func(names)
print(x)

"""
# 将1-100中能被3和5整除的数
num = [num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0]
print(num)
# 将0-5之间奇偶数组成元组
new_tiple = [(x, y) for x in range(6) if x % 2 == 0 for y in range(6) if y % 2 != 0]
print('new_tiple={}'.format(new_tiple))
'''
def yuanzu():
    new_tuple = []
    for i in range(6):
        if i % 2 == 0:  # 偶数
            for j in range(6):
                if j % 2 != 0:
                    new_tuple.append((i, j))
    return new_tuple


#调用
y = yuanzu()
print(y)
'''
