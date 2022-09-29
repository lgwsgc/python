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

# ------近几次课的总结--------
# 列表推导式 [表达式 for 变量 in 列表]
list1 = [1, 2, 3]  # ----> 列表
y = [x + 2 for x in list1]  # ----> 产生新的列表
print(y)
# 1.[表达式 for 变量 in 列表 if 条件]
y1 = [x + 2 for x in list1 if x % 2 == 0]
print(y1)
# 2.[结果A if 条件 else 结果B for 变量 in 列表 ]
y2 = [x + 2 if x % 2 == 0 else x + 1 for x in list1]
print(y2)


# -------y3解释y2------


def func():
    list_new = []
    for i in list1:
        if i % 2 == 0:
            i += 2
            list_new.append(i)
        else:
            i += 1
            list_new.append(i)
    return list_new


y3 = func()
print(y3)

# ------------------------------------
# 类中方法: 动作
# 种类: 普通方法 类方法 静态方法 魔术方法
# -------------------
'''
普通方法:
def 方法名(self,[,参数，参数]):
    pass
'''


class Phone1:
    brand = 'xiaomi'
    price = 4999
    type = 'Ultra'

    # Phone类里面方法名: call
    def call(self):
        print('self-------,', self)
        print('正在打电话...')
        print('这是我的note:', self.note)
        print('正在访问通讯录:')
        for person in self.address_list:
            print(person.items())
        print('正在打电话...')
        print('留言:',self.note)


phone2 = Phone1()
phone2.note = 'phone2'
phone2.address_list = [{'lgw': '15890716205'},
                       {'lx': '12345678'},
                       {'mcl': '8888888'}]
print(phone2, 'self-------1')
phone2.call()

phone3 = Phone1()
phone3.note = 'phone3'
phone3.address_list = [{'lgw': '15890716205'},
                       {'lx': '12345678'},
                       {'mcl': '8888888'}]
print(phone3, 'self-------2')
phone3.call()
