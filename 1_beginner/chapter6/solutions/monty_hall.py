"""
Monty Hall
Code the classic Monty Hall problem!

The following is a description of the Monty Hall Problem:
    There are three closed doors, 2 have goats behind them,
    only one has a car behind it.
    You don't know which door has what.
    The goal is to pick the door that has the car behind it.
    After you make a choice, Monty (the host) opens a door
    that you did not choose, revealing a goat.
    You are then asked whether you want to
    change your choice to the other door.
    The door you chose is more likely to have a car
    if you switch to the other door, apparently!

More step-by-step instructions (pseudocode) are commented below.

Read more about the Monty Hall Problem here:
https://betterexplained.com/articles/understanding-the-monty-hall-problem/
"""

# Make a list that represents the three closed doors,
# 'G' for the doors that have a goat, 'C' for the door that has a car.
import random
doors = ['G', 'G', 'C']

# Make the Monty Hall game repeat 6 times.
for i in range(6):
    # Randomize the doors
    random.shuffle(doors)

    # reset the doors left
    doors_left = [1, 2, 3]

    # The user enters their 1st choice
    print("A new Monty Hall game has begun!")
    choice = int(input("Choose from doors 1, 2, or 3...\n> "))
    doors_left.remove(choice)

    # A door that has a goat is revealed, cannot be the one user chose
    # makes a duplicate list to avoid messing up the original
    reveal_doors = doors.copy()

    # removes user's choice so that it won't be opened,
    # but keeps in the element to not mess up the indices
    reveal_doors[choice - 1] = '-'
    goat_door = reveal_doors.index('G') + 1
    doors_left.remove(goat_door)
    print("Monty opens door", goat_door, "to reveal a goat!")

    # The user is prompted to choose again
    print("With this new information, do you want to switch doors?")
    print("Your first choice was Door", choice)
    print("If you switch, you will be opening Door", doors_left[0])
    print("Enter 'y' to switch, or 'n' to keep your first choice.")
    switch = input("> ")

    if switch == 'y':
        choice = doors_left[0]

    # The prize behind the user's ultimate choice is revealed!
    if doors[choice - 1] == 'C':
        print("You got... a car! Congratulations!")
    else:
        print("You got... a goat! Better luck next time!")

    print()
