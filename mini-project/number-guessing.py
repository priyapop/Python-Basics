import random

no = random.randint(1,100)

while True:
    try:
        guess = int(input("Enter a number: "))
        if guess == no:
            print("you guessed it")
            break
        elif guess > no:
            print("guess lower")
        else:
            print("guess higher") 

    except ValueError:
        print("enter valid no")


    
   