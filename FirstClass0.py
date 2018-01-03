import random

def choice(n,m):
     if 1 <= int(m) <= int(n):
              return sorted(random.sample([i for i in range(1,int(n)+1)],int(m)))
     else:
         return "Please again sure!"
choice(100,10)


def main():
    print (choice)

main()
