# Guessing game
# Player have to guess the number with in 10 chances
# If number is guessed the program will terminate
# Player can quit the game by entering zero

import random

highest = 100
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0  # Initialize to any number outside of the valid range
count = 0
while guess != answer:
    guess = int(input())
    count += 1
    if guess == 0:
        break
    if count == 10:
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer: # Guess must be greater than the number
        print("Please guess lower")
    else:
        print("Well done, you guessed it")
print("Game Over")
