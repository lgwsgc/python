"""
递归函数: 不调用其他函数，而是调用自己，常用在查看文件
    递归错误：但递归层数过多，python就会报错
遵循：
1.必须有出口
2.每次递归要想出口靠近
"""
# 无出口，一直循环，会报错
# 递归格式


def text():
    print('------->')
    a()


def a():
    print('---a---')
    a()


# 设置出口，打印数字案例
def number(i, he):
    if i == 10:
        he += i
        print(he)
    else:
        print(i)
        he += i
        i += 1

        number(i, he)


number(1, 0)

flag = True
sum = 0
i = 1
while flag:
    if i <= 10:
        sum += i
        i = i + 1
    else:
        flag = False

print(sum)



# text()
