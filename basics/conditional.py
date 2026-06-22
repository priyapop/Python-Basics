#logic

# if 5 > 0:
#     print('yes')

# temp = 0
# if temp > 25:
#     print("It is really hot")
# elif temp >15:
#     print("its okay outside")
# else:
#     print("Its cold outside")


#mix color game

# color_one = input("enter colors 1").lower()
# color_two = input("enter colors 2").lower()

# if color_one == 'red' and color_two == 'blue' or color_one == 'blue' and color_two == 'red' :
#     print("New color is purple")
# elif color_one == 'yellow' and color_two == 'red':
#     print("New color is orange")
# elif color_one == 'red' and color_two == 'green':
#     print("New coloor is brown")
# else:
#     print("i dont know")

# color1 = input('Enter First Color (red, blue, yellow): ').lower()
# color2 = input('Enter Second Color (red, blue, yellow): ').lower()
# colors = [color1, color2]

# print('-'*50)
# print(f"🥼 Let's Mix {color1} + {color2}\n")

# #🎨 Calculate New Color
# if color1 == color2:
#     emoji = None
#     if color1 == 'red':
#         emoji = '❤️'
#     elif color1 == 'blue':
#         emoji = '💙'
#     elif color1 == 'yellow':
#         emoji = '💛'

#     print("🎨 You're mixing the same color!")
#     print(f'🧪{color1} + 🧪{color2} = {color1} {emoji}.')

# elif 'red' in colors and 'blue' in colors:
#     print(f'🧪{color1} + 🧪{color2} = Purple 💜.')

# elif 'red' in colors and 'yellow' in colors:
#     print(f'🧪{color1} + 🧪{color2} = Orange 🧡.')

# elif 'blue' in colors and 'yellow' in colors:
#     print(f'🧪{color1} + 🧪{color2} = Green 💚.')

# else:
#     print('❌ Invalid Color Combination. \nPlease use Red, Blue or Yellow.')

#guess number game

# secret = 5
# guess = int(input('Guess a number'))

# if guess == secret:
#         print("You are correct")

# elif guess > secret:
#     print("number is greater than secret number guess again \n")
    

# elif guess < secret:
#     print("number is less than secret number guess again \n")

#loops
# Guess a Number  !
import random

# Rules
# min_       = 1
# max_       = 20
# secret_num = random.randint(min_, max_) #Set any number you like!

# for i in range(5):
#     print('-'*50, f'Attempt {i+1}/5')

#     # Ask User for Input!
#     guess = input(f'Guess the secret number between {min_} and {max_}: ')
#     guess = int(guess)

#     # Check the Input
#     if guess < min_ or guess > max_:
#         print(f'Incorrect Input. Guess a number between {min_} and {max_}')

#     # Check Results
#     elif guess == secret_num:
#         print('Correct! You guessed it!')
#         break

#     elif guess > secret_num:
#         print(' Too High! Try Again.')

#     else:
#         print(' Too Low! Try Again.')


number_names = [
    "",         # 10^3
    "thousand",         # 10^3
    "million",          # 10^6
    "billion",          # 10^9
    "trillion",         # 10^12
    "quadrillion",      # 10^15
    "quintillion",      # 10^18
    "sextillion",       # 10^21
    "septillion",       # 10^24
    "octillion",        # 10^27
    "nonillion",        # 10^30
    "decillion",        # 10^33
    "Bajillion"         # 10^~ (I made this up...)
]

a = 0
b = 1

for i in range(100): 
    #print(f'{a:,d}')# comma every 3 digits for integer presentation
    num = f'{a:,d}'
    count_commas = num.count(',')
    large_num = number_names[count_commas]
    print(large_num,num)
    temp = a+b
    a= b
    b= temp
