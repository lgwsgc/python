# os.path 里面的函数
# os中的函数:
import os
# ---------------------查看当前文件所在文件夹-----------------
file_all = os.getcwd()
print(file_all)
# ---------------------查看当前文件所在文件夹-----------------
file_all = os.path.dirname(__file__)
print(file_all)
# ---------------------查看当前文件夹所有文件(所有同级目录)-----------------
file_list = os.listdir(file_all)
print(file_list)
# ---------------------创建文件夹-----------------
# if not os.path.exists(r'D:\Python\Git-python\p'):
#     f = os.mkdir(r'D:\Python\Git-python\p')  # (要创建的文件夹地址)
#     print(f)
# ---------------------删除文件夹-----------------
# f = os.rmdir(r'D:\Python\Git-python\p')  # 只能删除空文件夹
# print(f)
# ---------------------删除文件------------------
# os.remove(r'D:\Python\Git-python\p\a1.txt')
# ---------------------先删多个文件，再删文件夹-----------------
# path = r'D:\Python\Git-python\p'
# file_list_text = os.listdir(path)
# for file in file_list_text:
#     path1 = os.path.join(path,file)
#     os.remove(path1)
#     print('删除{}'.format(path1))
# else:
#     os.rmdir(path)
#
# print('删除成功')
# ---------------------切换文件夹-----------------
path = os.getcwd()
print(path)
f = os.chdir(r'D:\Python\pycham')
print(f)
path = os.getcwd()
print(path)
file_list = os.listdir(path)
print(file_list)
# ---------------------查看当前文件所在文件夹-----------------
# ---------------------查看当前文件所在文件夹-----------------
# ---------------------查看当前文件所在文件夹-----------------



