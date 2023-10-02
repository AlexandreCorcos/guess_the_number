import random
logo='''
                                                                   __ 
 _____                                 _____           _          |  |
|   __|_ _ ___ ___ ___    _____ _ _   |   | |_ _ _____| |_ ___ ___|  |
|  |  | | | -_|_ -|_ -|  |     | | |  | | | | | |     | . | -_|  _|__|
|_____|___|___|___|___|  |_|_|_|_  |  |_|___|___|_|_|_|___|___|_| |__|
                               |___|                                  
'''

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(player_num, comp_num, turns):
    if player_num > comp_num:
        print('Roo high')
        return turns - 1
    elif player_num < comp_num:
        print('Roo low')
        return turns - 1
    else:
        print(f'You win! The answer was {comp_num}')

def set_difficulty():
    level = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    comp_num = random.randint(1, 100)
    print(comp_num)
    turns = set_difficulty()
    player_num = 0
    while player_num != comp_num:
        print(f"You have {turns} attempts remaining to guess the number.")
        player_num = int(input('Make a guess: '))
        turns = check_answer(player_num, comp_num, turns)
        if turns == 0:
            print("You're run out of guesses, you lose.")
            return
        elif player_num != comp_num:
            print("Guess again.")

game()



