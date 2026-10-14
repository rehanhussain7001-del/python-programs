a=int(input("enter the value"))
b=int(input("enter the value"))
for i in range(1,1001):
    if(i%a == 0 and i%b == 0):
        print(i)
        break