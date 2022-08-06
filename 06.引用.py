# 在git bash中修改文件名称：git mv older_file new_file
# 引用就是地址传递
# del 变量  删除一个变量
import sys

a = 123
b = a
c = a
# reference
# print(sys.getrefcount(a))

list1 = [1, 2, 3, 4]
list2 = list1
list3 = list1

# print(sys.getrefcount(list1))  # 查询有多少个指针指向list1这个地址，它本身也算一个
# 通过id可以查看该变量的内存地址
# print(id(a))
print('-' * 30)


# 如果函数内n1发生变化，n1如果是可变类型则会变，否者就不变


def text1(n1):  # n1为整型，不变
    for i in range(n1):
        print('---->', i)
    n1 += 1


def text2(l):  # l为列表，可变
    for i in l:
        print('---->', i)
    l.insert(0, 5)


n = 9
list4 = [1, 2, 3, 4]
text1(n)
text2(list4)
print(n)
print('-' * 30)
print(list4)
