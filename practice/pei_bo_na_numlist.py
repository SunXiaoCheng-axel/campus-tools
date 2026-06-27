'''
裴波那契数列
输入正整数 n，输出斐波那契数列的前 n 项（前两项固定为 1、1，后续每项等于前两项之和）。
'''
def fibonacci(n):
    a, b = 1, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    print(fib_sequence)
#a,b=1,1   
#a,b,c=1,2,4
