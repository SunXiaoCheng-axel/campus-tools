while True:
    try:
        num = float(input('请输入一个整数：'))
        if num>0:
            print(f'您输入的整数是：正数{num}')
        elif num==0:
            print(f'您输入的整数是：零{num}')
        else:
            print(f'您输入的整数是：负数{num}')
        break
    except ValueError:
            print('输入错误，请输入一个整数！')
