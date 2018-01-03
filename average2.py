#average2.py

print("********average2**********")
def main():
    sum = 0.0
    count = 0.0
    moredata = "yes"
    #print("Or not moredata?",moredata)
    while moredata[0] == "y":
        x = eval(input("Enter a number>>\n"))
        sum = sum + x
        count =+ 1
        moredata = input("Do you have more numbers(yes or no)?")
        print("\nThe average of the number is",sum/count)
        #if moredata == "yes":
            #y = eval(input("Please input the num:\n"))
           #sum =+ y
            #count =+ 1
            #print("result:",sum/count)
        #else :
           # print("result:",sum/count)
            
main()
