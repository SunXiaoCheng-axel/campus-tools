#预设答案数字（如 66），用户循环输入数字猜测，程序提示「猜大了」「猜小了」「猜对了」，猜对则结束程序。
'''
用random模块生成随机数之前要先导入random模块
random.uniform(a,b)可以生成a到b之间的随机浮点数
random.random()生成0到1之间的随机浮点数
左闭右开区间整数 random.randrange (start, stop, step)   
random.randint(a,b)可以生成a到b之间的随机整数
列表随机抽取一个数字 random.choice ()
nums = [10,20,30,40]
res = random.choice(nums)
print(res)
'''
import random
target = random.randint(1, 101)
num=int(input("请输入你猜的数字（1~100）："))
while num != target:
    if num > target:
        print("猜大了")
    else:
        print("猜小了")
    num=int(input("请重新输入你猜的数字（1~100）："))
print("猜对了")
