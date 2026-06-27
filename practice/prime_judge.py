#输入一个大于 2 的正整数，判断它是否为素数（质数：只能被 1 和自身整除的数）。
n = int(input("请输入一个大于 2 的正整数："))
for i in range(2, n):
    if n % i == 0:
        print(n, "不是素数")
        break
else:
    print(n, "是素数")