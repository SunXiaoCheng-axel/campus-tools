'''
冒泡排序
给定数字列表 [9, 3, 1, 5, 7, 2, 8]，使用冒泡排序算法将列表从小到大排序并输出结果。
python中四种函数写法：
1.无参无返回值函数
   def bubble_sort():
       print("冒泡排序")
    dubble_sort()
2.有参无返回值函数
    def bubble_sort(lst):
         print("冒泡排序")
         print(lst)
     bubble_sort([9, 3, 1, 5, 7, 2, 8])
3.无参有返回值函数
    def bubble_sort(): 
        print("冒泡排序")
         return [9, 3, 1, 5, 7, 2, 8]
    result = bubble_sort()
4.有参有返回值函数
    def bubble_sort(lst):
        print("冒泡排序")
        return lst
    result = bubble_sort([9, 3, 1, 5, 7, 2, 8])
'''
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print("排序后的列表：", lst)
