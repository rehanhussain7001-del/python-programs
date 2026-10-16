email=input("tell me your email")
if '@' in email :
    password=input("tell me your password also")
    if email == "rehan4678@gmail.com" and password == "1234":
        print("welcome")
    elif email == "rehan4678@gmail.com" and password != "1234":
        print("password is incorrect")
        password = input("enter your password again")
        if password == "1234":
            print("now it is correct")
        else :
            print("still wrong password")
    else :
        print("the information is wrong")
else:
    print("your email is wrong . please correct it .")    