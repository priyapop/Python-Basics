import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {ROCK:'🪨',PAPER:'📃',SCISSORS:'✂️'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        userInput =input("rock, paper scissors?(r/p/s):").lower()
        if userInput  in choices:
            return userInput
            
        else:
           print("enter valid input")

def display_choices(userInput,computer_choice):
    print(f'You chose {emojis[userInput]}')
    print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(userInput,computer_choice):
    if userInput == computer_choice:
        print('tie!!')
    elif(
        (userInput == ROCK and computer_choice ==SCISSORS) or 
        (userInput==PAPER and computer_choice==ROCK)or 
        (userInput==SCISSORS and  computer_choice==PAPER)):
        print('you win')
    else:
        print('you lose')


def play_game():
    while True:
        userInput = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(userInput,computer_choice)

        determine_winner(userInput,computer_choice)

        should_continue=input('Continue? (y/n):').lower()
        if should_continue=='n':
            break
        
play_game()