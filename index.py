import random
num=random.randint(1,100)
count=0
first_guess=True
while count<10:
    if first_guess:
        guess = int(input("Enter your guess between 1-100: "))
        first_guess = False
    else:
        guess = int(input("Try again: "))
    if 0<guess<=100:
        count+=1
        if guess<num:
            print("Higher!")
        elif guess>num:
            print("Lower!")
        else:
            print("You are correct!")
            print(f"your trials are:{count}.")
            break
    else:
        print("Enter a valid number.")
else:
    print(f"Your are done with your trial, your number was{num}.")            