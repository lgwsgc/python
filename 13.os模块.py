# os.path 里面的函数
# os中的函数:
import os
# ---------------------查看当前文件所在文件夹-----------------
# file_all = os.getcwd()
# print(file_all)
# ---------------------查看当前文件所在文件夹-----------------
# file_all = os.path.dirname(__file__)
# print(file_all)
# ---------------------查看当前文件夹所有文件(所有同级目录)-----------------
# file_list = os.listdir(file_all)
# print(file_list)
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
# path = os.getcwd()
# print(path)
# f = os.chdir(r'D:\Python\pycham')  # 切换文件夹
# print(f)
# path = os.getcwd()  # 查看是否切换成功
# print(path)
# file_list = os.listdir(path)  # 查看切换后文件夹目录
# print(file_list)
# ---------------------复制文件夹(只能复制单层文件夹，文件夹中套文件夹则不行， 需优化)-----------------
# src_path = r'files'
# target_path = r'files2'
# 封装成函数


# def copy_func(src, target):
#     if os.path.isdir(src) and os.path.isdir(target):
#         fileList = os.listdir(src)  # 将文件以列表形式返回
#         print(fileList)
#         for file in fileList:
#             path = os.path.join(src, file)
#             print(path)
#             with open(path, 'rb') as stream_in:
#                 container = stream_in.read()
#
#                 path1 = os.path.join(target,file)
#                 with open(path1, 'wb') as stream_out:
#                     stream_out.write(container)
#
#     else:
#         print('复制完成')
#
#
# copy_func(src_path, target_path)
# ---------------------复制文件夹(可解决文件夹中套文件夹，但新的文件夹中的内容会统一放到一起，不会像原目录， 需优化)
# src_path = r'files'
# target_path = r'files2'
# # 封装成函数
#
#
# def copy(src_path, target_path):
#     # 获取文件夹的内容
#     fileList = os.listdir(src_path)
#     # 变量列表
#     print(fileList)
#     for file in fileList:
#         # 拼接路径
#         path = os.path.join(src_path, file)
#         print(path)
#         # 判断是文件夹还是文件
#         if os.path.isdir(path):
#             # os.chdir(path)
#             # 调用函数(递归)
#             copy(path, target_path)
#         else:
#             # 是文件则直接进行复制
#             with open(path, 'rb') as stream_in:
#                 container = stream_in.read()
#
#                 path1 = os.path.join(target_path, file)
#                 with open(path1, 'wb') as stream_out:
#                     stream_out.write(container)
#     else:
#         print('复制完成')
#
#
# copy(src_path, target_path)
# ---------------------查看当前文件所在文件夹-----------------
# src_path = r'files'
# target_path = r'files2'
# # 封装成函数
#
#
# def copy(src_path, target_path):
#     # 获取文件夹的内容
#     fileList = os.listdir(src_path)
#     # 变量列表
#     print(fileList)
#     for file in fileList:
#         # 拼接路径
#         path = os.path.join(src_path, file)
#         print(path)
#         # 判断是文件夹还是文件
#         if os.path.isdir(path):
#             # os.chdir(path)
#             # 调用函数(递归)
#             target_path1=os.path.join(target_path, file)
#             os.mkdir(target_path1)
#             copy(path, target_path1)
#         else:
#             # 是文件则直接进行复制
#             with open(path, 'rb') as stream_in:
#                 container = stream_in.read()
#
#                 path1 = os.path.join(target_path, file)
#                 with open(path1, 'wb') as stream_out:
#                     stream_out.write(container)
#     else:
#         print('复制完成')
#
#
# copy(src_path, target_path)
# --------------------------------------------------------------
src_path = r'files'
target_path = r'files2'
# 封装成函数


def copy(src_path, target_path):
    # 获取文件夹的内容
    fileList = os.listdir(src_path)
    # 变量列表
    print(fileList)
    for file in fileList:
        # 拼接路径
        path = os.path.join(src_path, file)
        print(path)
        # 判断是文件夹还是文件
        if os.path.isdir(path):
            # os.chdir(path)
            # 调用函数(递归)
            # 这里的路径是要改成目标路径
            path2 = os.path.join(target_path, file)
            # 在目标路径创建文件夹
            os.mkdir(path2)
            # 调用递归函数
            copy(path, path2)

        else:
            # 是文件则直接进行复制
            with open(path, 'rb') as stream_in:
                container = stream_in.read()

                path1 = os.path.join(target_path, file)
                with open(path1, 'wb') as stream_out:
                    stream_out.write(container)
    else:
        print('复制完成')


copy(src_path, target_path)


