records=[(101,"alice",50000),(102,"bob",65000),(103,"charlie",45000)]
empid=int(input("enter the employee id to be searched"))
for i in records:
    if empid in i:
            print("correct id")
            break
    if empid not in i:
        print("wrong id")

     