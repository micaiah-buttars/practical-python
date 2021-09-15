import random

comp_choice = random.choice(['scissors', 'paper', 'rock'])
user_choice = input('rock, paper, or scissors?\n')

win = 'WIN: ' + user_choice + " beats " + comp_choice
lose = 'LOSE: ' + comp_choice + " beats " + user_choice

if comp_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and comp_choice == 'scissors':
    print(win)
elif user_choice == 'paper' and comp_choice == 'rock':
    print(win)
elif user_choice == 'scissors' and comp_choice == 'paper':
    print(win)
else:
    print(lose)