'''
账号密码验证
预设正确用户名 admin、密码 123456，用户最多有 3 次输入机会；输错提示剩余次数，3 次全错则提示账号锁定，输入正确则提示登录成功。
'''
username = "admin"
password = "123456"
for attempt in range(3):
    input_username = input("请输入用户名：")
    input_password = input("请输入密码：")
    if input_username == username and input_password == password:
        print("登录成功！")
        break
    else:
        remaining_attempts = 2 - attempt
        if remaining_attempts > 0:
            print(f"用户名或密码错误，您还有 {remaining_attempts} 次机会。")
        else:
            print("账号已锁定，请联系管理员。")