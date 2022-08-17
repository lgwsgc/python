"""
异常: 运行时爆出错误，xxxError
异常处理:
格式：
    try:
        可能出现异常的代码
    except:
        如果有异常执行的代码
    finally:
        无论一场是否存在都会执行的代码

case1:
    try:
        可能出现异常的代码
    except case1:
        如果有异常执行的代码
    except case2:
        如果有异常执行的代码
    ...
    except exception as err:
        print('出错了'，err)  # 可打印出位置错误类型，(除了已知的异常，剩下的都归为此类)
    finally:
        无论一场是否存在都会执行的代码

case2:获取Exception的错误原因
    try:
        可能出现多种异常的代码
    except case1:
        如果有异常执行的代码
    except case2:
        如果有异常执行的代码
    ...
    except exception as err:
        print(err)  # ---》err的内容就是错误原因
    finally:
        无论一场是否存在都会执行的代码

case3:获取Exception的错误原因
    try:
        可能出现多种异常的代码
    except case1:
        如果有异常执行的代码
    except case2:
        如果有异常执行的代码
    ...
    except exception as err:
        print(err)  # ---》err的内容就是错误原因
    else:
        print('-----')  # 没有异常才会执行的代码

case4:
    常用于文件操作 stream = open(url) stream.read() stream.close()

    try:
        可能出现多种异常的代码
    except case1:
        如果有异常执行的代码
    except case2:
        如果有异常执行的代码
    ...
    except exception as err:
        print(err)  # ---》err的内容就是错误原因
    finally:
        print('-----')  #

"""


def func():
    try:
        num1 = int(input("数字一:"))
        num2 = int(input("数字二:"))
        # 判断符号
        per = input('请输入符号(+ = * /):')
        if per == '+':
            # + 加法
            sum_num = num1 + num2
            print('sum= ', sum_num)
        elif per == '-':
            # - 减法
            red_num = num1 - num2
            print('reduce= ', red_num)
        elif per == '*':
            # * 乘法
            mul_num = num1 * num2
            print('multiplication= ', mul_num)
        elif per == '/':
            # / 除法
            div_num = num1 / num2
            print('division= ', div_num)
        else:
            print('符号输入有误！！！')
        # list1 = []
        # list1.pop()  # 空列表不能弹出，故意写出，查看错误原因
    except ZeroDivisionError:
        print('除数不能为0！')
    except ValueError:
        print('请输入数字! ')
    except Exception as err:
        print(err)
    finally:
        print('结束')


# func()

# ---------case4------------
def func_file():
    stream = None
    try:
        stream = open('manage_books/books.txt', encoding='utf-8')
        container = stream.read()
        print(container)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('----------finally-----------')
        if stream:
            stream.close()
        return 3


# 调用
# x = func_file()  # finally比较特殊，return会返回finally中的返回值，覆盖掉之前的return
# print(x)


# -----------自定义错误，抛出异常---------------------
# raise (异常)
def register():
    username = input('请输入用户名:')
    if len(username) < 6:
        raise Exception('用户名长度需在6位以上')
    else:
        print('输入的用户名是:{}'.format(username))


# register()
try:
    register()
except Exception as err:
    print(err)
    print('注册失败')
else:
    print('注册成功')