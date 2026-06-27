#输入一个正整数n，计算n的阶乘（n! = 1*2*3*...*n）
try:
    n= int(input("请输入一个正整数n："))
    if n<0:
        print("输入错误，请输入一个正整数！")
    else:
        factorial =1
        for i in range(1,n+1):
            factorial *= i
        print(f"{n}的阶乘是：{factorial}")
except ValueError:
    print("输入错误，请输入一个正整数！")
    