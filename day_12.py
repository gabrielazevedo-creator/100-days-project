# Guess the number

import random
from time import sleep

# generate a random integer number
# player types guesses and computer gives hints (too high), (too low)

while True:
    attempts = 0

    difficulty = input('1- Easy\n2- Hard\n')
    if difficulty == '1':
        attempts = 10
    elif difficulty == '2':
        attempts = 5
    else:
        print('Wrong choice.')
        continue
    mysterious_number = random.randint(1,100)
    print('...')
    sleep(0.3)
    print('A mysterious number from 1 to 100 was generated. Try guessing it.')


    while True:
        print(f'Remaining attempts: {attempts}')
        guess = int(input('Enter the guess: '))
        if guess > mysterious_number:
            print('Too high.')
            attempts -= 1
        if guess < mysterious_number:
            print('Too low.')
            attempts -= 1
        if guess == mysterious_number:
            print('You guessed the mysterious number.')
            break
        if attempts == 0:
            print('You have no more attempts left. You lose.')
            break

    play_again = input('Do you want to play it again? [Y/N]\n').strip().lower()
    if play_again == 'y':
        continue
    else:
        break
