# without using title we have to make every first character of a word capital 
str = input("enter the string")
a = str.split()
print(a)
L = []
for i in a :
    print(i.capitalize())
    L.append(i.capitalize())  
print(L)
str_2=" ".join(L)
print(str_2)
