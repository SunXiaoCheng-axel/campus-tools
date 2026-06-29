
def xunhuanshu(n):
    while True:
            if(n>0 and n%1==0):
                for i in range(2,n+1,2):
                    print(i)
                break
            else:
                print('输入无效，请输入正整数')



           
#finally与except