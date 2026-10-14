list=[101,105,102,101,108,105,110]
for i in list:
    if list.count(i) > 1 :
        continue
    if list.count(i) == 1 :
        print(i)

