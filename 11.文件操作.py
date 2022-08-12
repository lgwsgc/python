# 文件操作
"""
文件上传
保存log

mode:r w 纯文本文件
     rb wb  图片,电影,音乐
     b: binary 二进制

缓存: 调节cpu和硬盘之间的速度

系统函数:
    open(file,mode,buffering,encodeing)

r: 读操作   方法 read() 读取所有内容
               readline()读取每一行内容
               readlines() 读取所有行保存到列表中
               readable() 判断是否可读
               非文本一般使用rb

w：写操作   方法: write(内容) 每次都会将原来的内容清空，然后再写当前的内容
                writelines(['赌神'，'赌侠'，'赌圣'])
a: 追加，不会清空原来的内容
"""
# 读文件 stream = open('path/filename','r') ---->返回值:stream (管道)
#       container = stream.read()----->读取管道的内容
#       如果传递的path/filename有误，则会报错，FileNotFoundError
# -----------打开文件(默认是只读)--------------------------------
# stream = open(r'D:\Python\Git-python\files\text.txt')  # r: 取消字符串中的所有可能转义，即字符串的所有字符都会被当成正常字符。
# stream0 = open('files/text.txt')  # 需要用引号引住地址
# -----------读取文本文件，并打印-----------------
# container0 = stream0.read()
# print(container0)
# -----------判断文本文件是否可读，并打印-----------------
# container1 = stream0.readable()  # 判断是否可读
# print(container1)
# -----------通过循环，逐行读取文本文件，并打印-----------------
# while True:
#     line = stream0.readline()  # 每次读一行，如果已经读过，则不会显示
#     print(line)
#     if not line:
#         break
# -----------读取文本文件并保存到列表，通过for循环打印-----------------
# lines = stream0.readlines()  # 保存到列表中
# print(lines)
# for i in lines:
#     print(i)
# ------------读取图片，并打印，这里无法直接打印出图片，而是以二进制形式打印的--------------------
# photo = open(r"D:\Python\Git-python\files\0.bmp", 'rb')
# photo_container = photo.read()
# print(photo_container)
# ------------关闭该文件--------------------
# stream0.close()


# ------- 写文件，进行写操作------------------
# stream = open(r'D:\Python\Git-python\files\text.txt', 'w')  # r: 取消字符串中的所有可能转义，即字符串的所有字符都会被当成正常字符。
# s = '''你好！
#     欢迎来到澳门博彩赌场，赠送给你金币一枚
#                     赌王:周润发
# '''
# ------将s的内容写入文件-----------
# result = stream.write(s)
# print(result)
# stream.write('龙武')
# -------直接写入: 内容-----------
# result = stream.write('hello')
# print(result)
# result1 = stream.write('凹凸曼')
# print(result1)
# stream.writelines('凉子同学')
# stream.writelines(['赌神', '赌侠', '赌圣'])  # 不会直接换行
# stream.writelines(['赌神\n', '赌侠\n', '赌圣\n'])  # 需要手动添加: \n
# ----续写文件--------------
# stream = open('D:\\Python\\Git-python\\files\\text.txt', 'a')  # \\: 和r类似，取消字符串中的所有可能转义，即字符串的所有字符都会被当成正常字符。
# t = '''---------
# 通知:
#     你因太帅被通缉，现命你好好学习a
#                     外貌协会
# ---------------'''
# res = stream.write(t)
# print(res)
# -----------文件的复制-------------
'''
原文件: D:\\Python\\Git-python\\files\\text.txt
目标文件: D:\\Python\\Git-python\\files2\\text.txt

with 结合open使用，可以帮助我们自动释放资源
'''
# file_in = open('D:\\Python\\Git-python\\files\\text.txt', 'rb')
# 等价于 with open('D:\\Python\\Git-python\\files\\text.txt', 'rb') as file_in
# ----------------复制单个文件-----需要先写好要复制到拿个文件里，如下面案例: 写在txt文件中--------------------------------------------
# with open(r'D:\Python\Git-python\01.function.py', 'rb') as file_in:
#     container_in = file_in.read()  # 读取文件内容
#     with open('D:\\Python\\Git-python\\files2\\text.txt', 'wb') as file_out:
#         file_out.write(container_in)
#
# print('复制完成')
# ----------------批量复制文件(也就是文件夹)-----需要引入os模块------
# 模块: xxx.py 如: os.py
import os
'''
os.path:
path = os.path.dirname(__file__)  # 获取当前文件所在的文件目录(绝对路径: 具体路径: 从某盘到具体目录文夹)
os.path.join(path, 'text_one.txt')
'''
# print(os.path)
# path = os.path.dirname(__file__)  # 获取当前文件所在的文件目录(绝对路径: 具体路径: 从某盘到具体目录文夹) --->D:\Python\Git-python
# print(path)
# print(type(path))


with open(r'D:\Python\Git-python\files\0.bmp', 'rb') as file_in:
    container_in = file_in.read()  # 读取文件内容
    print(file_in.name)
    file = file_in.name
    filename = file[file.rfind('\\')+1:]  # 截取文件名
    print(filename)
    # path = os.path.dirname(__file__)
    paths = os.path.join(r"D:\Python\Git-python\files2", filename)
    with open(paths, 'wb') as file_out:
        file_out.write(container_in)

print('复制完成')

# -------关闭文件，释放资源------------
# stream.close()
