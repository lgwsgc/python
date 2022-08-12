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
    
"""
stream = open(r'D:\Python\Git-python\files\text.txt')  # r: 取消字符串中的所有可能转义，即字符串的所有字符都会被当成正常字符。
container = stream.read()

print(container)
