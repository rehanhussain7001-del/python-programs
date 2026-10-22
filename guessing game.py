import random
guess_number = random.randint(1,100)
guess = int(input("guess the number "))
attempts = 1
while guess != guess_number :
    if guess < guess_number :
        print("guess higher")
    else:
        print("guess lower")
    guess = int(input("guess the number "))
    attempts += 1
print("correct answer")
print("attempts taken ",attempts)