# average2.py

n = eval(input("How many numbers?"))
sum = 0.0
for i in range(n):
    x = eval(input("Enter a numbers >>"))
    sum = sum + x
print("\nThe average is ",sum/n)
