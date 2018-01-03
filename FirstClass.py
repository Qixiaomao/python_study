#从1~n中，随机取m个数。1<=m<=n

#import random

from random import *

def main():
    m = eval(input("需要几个数："))
    n = eval(input("最大值："))
    if 1 <= int(m)<= int(n):
        for i in range(m):
            num = int(randint(1,n))
            print (num)
    else :
        print("请确认最大值超过所需数字个数！")

main()
