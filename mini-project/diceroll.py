import random

while True:
    ans = input("enter y/n to roll dice: ").lower()
    if ans == 'y':
        print(random.randint(1,6),random.randint(1,6))
    elif ans == 'n':
        print("thank you for playing")
        break
    else:
        print("invalid choice")