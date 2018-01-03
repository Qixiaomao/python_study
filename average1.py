# average1.py

print("*******average1******\n")
n = eval(input("Please input some nums:"))
sum = 0
av = 0
for i in range(n):
    x = eval(input("Please input the x:\n"))
    sum = sum + x
    av = sum/n
print("result:{}".format(av))
