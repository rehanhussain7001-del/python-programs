# for example number = 49 then sum = 4 + 9 =13
number = int(input("enter the digit or number"))
sum_digits = 0
while number > 0 :
    digit = number % 10
    sum_digits += digit
    number = number // 10
print("sum of the digits is", sum_digits)