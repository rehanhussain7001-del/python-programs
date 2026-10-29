# to remove repeated items from a list 
l1= [1,2,2,3,4,5,3,4,6,8,2,2]
l2= []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)