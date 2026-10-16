# series formula : 1/1! + 2/2! +3/3! + .... ..... .....
n = int(input("enter the number"))
sum = 0 
fact = 1
for i in range(1 , n + 1) :
    fact *= i
    sum += i/fact
print("the sum of the series is ",sum)
