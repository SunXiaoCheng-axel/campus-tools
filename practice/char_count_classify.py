#用户输入一行任意字符串，统计并输出其中英文字母、数字、空格、其他字符的数量。
def char_count_classify():
    s = input("请输入一行任意字符串：")
    letter_count = 0
    digit_count = 0
    space_count = 0
    other_count = 0

    for char in s:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1

    print("英文字母数量：", letter_count)
    print("数字数量：", digit_count)
    print("空格数量：", space_count)
    print("其他字符数量：", other_count)
'''
isalpha()判断单个字符是否为字母
isdigit()判断单个字符是否为数字
isspace()判断单个字符是否为空格
isupper()判断单个字符是否为大写字母
islower()判断单个字符是否为小写字母
'''