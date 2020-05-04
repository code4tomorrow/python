# Guess
# Import the random module.
# Store a random secret number in a variable
# called secret_number (use randrange or randint).
# The secret number should be from 1 to 20 (inclusive).
# Ask the user to keep guessing the number until they
# get it right. (You might want to print messages
# to tell the user if they guessed right or wrong.)

import random

secret_number = random.randrange(1, 21)

while True:
    guess = int(input("Enter your guess (number from 1-20): " ))
    if guess == secret_number:
        print("Congratulations, you guessed right!")
        break
    print("Oops, that's not right! Keep guessing.")