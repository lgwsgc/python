# 持久化保存: 文件
# list, tuple, dict----->内存，非持久化

# 用户注册
def register():
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    re_password = input('请再次确认密码: ')
    if password == re_password:
        # 保存信息
        with open(r'manage_books\user.txt', 'a') as stream_out:
            stream_out.write('{} {}\n'.format(username, password))

        print('用户注册成功！')
    else:
        print('密码不一致')


# 用户登录
def login_in():
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    if username and password:
        with open(r'manage_books/user.txt') as stream_in:
            while True:
                user_read = stream_in.readline()

                if not user_read:
                    print('用户名或密码错误，是否重新输入')
                    break

                input_user = '{} {}\n'.format(username, password)
                if user_read == input_user:
                    print('用户登录成功')
                    break

                # else:
                #     print('用户名或密码错误，是否重新输入')
                #     answer = input('请输入(y|n):')
                #     if answer == 'y':
                #         login_in()


# 图书展示
def show_books():
    print('-' * 20 + '图书馆图书展示' + '-' * 20)
    with open(r'manage_books/books.txt', encoding='utf-8') as stream_in:
        books = stream_in.readlines()
        # date = ''.join(date).strip('\n')  去掉换行
        for book in books:
            # print('{}'.format(book), end='')
            book = ''.join(book).strip('\n')
            print('《{}》'.format(book), end='\n')


# 调用函数
# register()
# login_in()
# show_books()

# 图书馆借书案例 亟待完善
def borrow_books():
    # global username
    # global password
    userd = input('是否已经注册账号(y|n):')
    if userd == 'y':
        login_in()
        show_books()
        search_book = input('请输入借阅书籍: ')
        print('《'+search_book+'》')
        with open('manage_books/user_book.txt', 'a') as book_in:
            book_in.write('username: '+search_book+'\n')
        print('借书完成')

    else:
        register()
        borrow_books()


borrow_books()
