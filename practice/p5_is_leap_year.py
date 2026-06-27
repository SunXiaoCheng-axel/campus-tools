'''
给定一个年份，判断该年份是否为闰年并输出结果。
规则：能被 4 整除但不能被 100 整除，或者能被 400 整除的年份是闰年。
'''
num = int(input("请输入年份："))
if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print(num, "是闰年")
else:
     print(num, "不是闰年")


'''
判断一个随机的年费是否为闰年
'''
import random
year = random.randint(1900,2100)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "是闰年")
else:
        print(year, "不是闰年")