# -----------------列表推导式1(除了列表，还有字典，集合)-----------------------------
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
mul = []
# -----------------列表推导式2-----------------------------
dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'tony', 'salary': 8000}
dict3 = {'name': 'jack', 'salary': 4500}
dict4 = {'name': 'lily', 'salary': 3000}

list1 = [dict1, dict2, dict3, dict4]  # [{},{},{},{}]


# 如果薪资大于5000涨200，小于等于5000涨500
newlist1 = [{staff['name']: staff['salary'] + 200} if staff['salary'] > 5000 else {staff['name']: staff['salary'] + 500} for staff in list1]
# print(newlist1)
# --------------------------------------------------------------
# def pailie(list1):
#     newlist1 = []
#     for staff in list1:
#         if staff['salary'] > 5000:
#             staff['salary'] += 200
#             newlist1.append({staff['name']: staff['salary']})
#         else:
#             staff['salary'] += 500
#             newlist1.append({staff['name']: staff['salary']})
#     return newlist1

# 调用
# x = pailie(list1)
# -----------------------------------------------------------------
print('newlist1={}'.format(newlist1))

# ----------------集合推导式-----------------------------
list2 = [1, 3, 2, 4, 1, 2, 6, 7]

set1 = {x for x in list2 if x > 4}
print(set1)
# ----------------字典推导式-----------------------------
dict5 = {'a': 'A', 'b': 'B', 'c': 'C'}

newdict = {value: key for key, value in dict5.items()}
print(newdict)
