# Python校园工具主程序
import practice.pei_bo_na_numlist
from practice.mao_pao_sort import bubble_sort
from practice.char_count_classify import char_count_classify
def main():
    print("欢迎使用Python校园工具")
    print("1. 斐波那契数列")
    print("2. 冒泡排序")
    print("3. 字符统计与分类")
    choice = input("请输入功能编号：")
    if choice == "1":
        practice.pei_bo_na_numlist.fibonacci(12)
    elif choice == "2":
        practice.mao_pao_sort.bubble_sort([9, 3, 1, 5, 7, 2, 8])
    elif choice == "3":
        char_count_classify()
    else:
        print("无效的选择，请重新运行程序。")
if __name__ == "__main__":
    while True:
        main()
        cont = input("是否继续使用工具？(y/n): ")
        if cont.lower() != 'y':
            print("感谢使用Python校园工具，再见！")
            break
