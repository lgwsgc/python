"""
return 返回值
1.return后面可以是一个参数，接收的是x = add(a, b)
2.return后面可以是多个参数，如果是多个参数，则底层会将多个参数放到一个元组中，将元组作为整体返回
3.接收的容器也可以是多个，如果容器和参数个数相同，则会，一一对应，依次放入
"""


# 函数的返回值:函数运算的结果 通过return“扔”出来，需要通过一个容器来接，不然无法显示


def add(a, b):
    result = a + b
    print(result)  # 只能在终端使用，外界调用不了

    return result, 100


# x, y = add(2, 6)
# print(x, y)

"""
用户登录
输入用户名
输入密码
输入验证码 ---》封装成一个函数

"""
import random


# 定义验证码函数
def generate_checkcode(n):
    s='0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(n):
        ran = random.randint(0, len(s)-1)
        code += s[ran]
    return code


def Login():
    uname0 = 'lgw'
    pwd0 = '123'
    uname = input("输入用户名:")
    pwd = input("输入密码:")
    # 获得一个验证码
    code = generate_checkcode(4)
    print("验证码是{}，请输入验证码".format(code))
    code1 = input("输入验证码:")
    # 验证
    if code.lower() == code1.lower():
        # 验证码输入正确
        if uname == uname0 and pwd == pwd0:
            print("登陆成功")
        else:
            print("用户名或者密码输入有误！")
    else:
        print("验证码输入有误！")


Login()
"""
函数嵌套调用:

"""
is_login = False  # 用于判断用户是否登录成功
flag = True


def add_shoppingcart(goods_name):
    global is_login
    if is_login:
        if goods_name:
            # 登陆成功
            print("成功将{}加入到购物车中！".format(goods_name))
        else:
            print("未添加任何商品")
    else:
        # 登录失败
        print("登录失败，是否重新登录(y|n)")
        Anwser = input("请输入:")
        if Anwser == 'y':
            username = input("请输入用户名：")
            password = input("请输入密码：")
            # 调用登录函数
            is_login = login(username, password)
            print('is_login:', is_login)

        else:
            print('很遗憾，不能添加任何商品！！！')


def login(uname, pwd):
    if uname == 'admin123' and pwd == '123456':
        # 登陆成功
        return True
    else:
        # 登录失败
        # print("用户名或者密码错误")
        return False


# 调用函数: 将商品添加到购物车中
# username = input("请输入用户名：")
# password = input("请输入密码：")
# is_login = login(username, password)
# add_shoppingcart("迪奥999")
