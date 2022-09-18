"""
面向对象:
    程序:----->现实中
    对象:----->具体的事物

现实中事物----》转成电脑程序
世间万物皆对象

好处:
    面向对象： 类  对象  属性  方法

    对象:
        x的手机
        y的手机
        z的手机 ...

        对象的集合 ---》共同特征(手机类)：品牌，颜色，大小，价格        动作: 打电话 发短信 上网 打游戏...
        类别：1.手机类
             2.学生类
             李岗威 张海洋 陈红艳 陈宇鹏
             特征: 姓名 年龄 性别 身高... --->属性
             动作: 刷抖音 打游戏 看书...  --->方法

        多个对象 ----》提取对象的共同特征和动作 ----》封装到一个类中

"""
# 类名要求首字母大写，多个单词采用驼峰式命名
# ValueError TypeError StopIteration
'''
class 类名[(父类)]:
    属性: 特征
    
    方法: 动作
'''


class Phone:
    # 属性
    # pass
    brand = 'xiaomi'
    # 方法


# 使用类创建对象:
lgw = Phone()
print(lgw)
print(lgw.brand)
mcl = Phone()
print(mcl)
mcl.brand = 'iphone'
print(mcl.brand)
dmy = Phone()
print(dmy.brand)


# --------------定义类和属性-----------------


class Student:
    # 类属性
    name = 'lgw'
    age = 23


# --------------创建和使用类-----------------
lgw = Student()
# 对象属性，先找自己空间的，再去类模型中找，均没有则报异常
lgw.age = 18  # 动态创建对象属性，此为赋值操作，针对该对象，对类属性无效
lgw.gender = "boy"
print(lgw)
print(lgw.gender)
print(lgw.name)
print(lgw.age)
mt = Student()
print(mt.name)
print(mt.age)
mt.name = 'mt'
print(mt.name)
# -----修改类属性(相当于全局)----
Student.name = 'SGC'
print(lgw.name)

