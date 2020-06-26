
for i in range(4):
    user_name = input('输入用户名: ').strip()
    password = input('密码: ').strip()
    if (user_name == 'alex' or user_name == 'seven')and password == '123':
            break
    else:
        print('密码错误')