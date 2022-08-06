# 注释
def login(uname, pwd):

    """
     用户登录
    :param uname: 用户名
    :param pwd: 密码
    :return: 是否登陆成功
    """

    if uname == 'admin123' and pwd == '123456':
        print('登陆成功')
        return True
    else:
        # 登录失败
        print("用户名或者密码错误")
        return False


login('admin123', '123456')
