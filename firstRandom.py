#firstRandom.py
#从1~n中选取m个数，1<=m<=n


import random

def main():
    print("*************************\n")
    print("***      随机取数     ***\n")
    print("提示：请在1~n中选择m个数 \n")
    print("要求：1<=m<=n            \n")
    m = eval(input("请输入选择的数：\n"))
    n = eval(input("请输入总数：    \n"))
    if 1<= int(m) <= int(n):
        print("结果有:{}".format(random.sample(range(1,n),m)))
    else :
        print("请确认输入的数不大于该要求！")


main()
