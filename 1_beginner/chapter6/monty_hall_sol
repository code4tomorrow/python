"""
Code the classic Monty Hall problem!
The following is a description of the Monty Hall Problem:
    There are three closed doors, 2 have goats behind them, only one has a car behind it.
    You don't know which door has what. The goal is to pick the door that has the car behind it.
    After you make a choice, Monty (the host) opens a door that you did not choose, revealing a goat. 
    You are then asked whether you want to change your choice to the other door.
    The door you chose is more likely to have a car if you switch to the other door, apparantly!
More step-by-step instructions are commented below.
Read more about the Monty Hall Problem here: (https://betterexplained.com/articles/understanding-the-monty-hall-problem/)
"""
#Make a list that represents the three closed doors, 'G' for the doors that have a goat, 'C' for the door that has a car.
import random
monty_hall = ['G', 'G', 'C']

#Make the Monty Hall game repeat 6 times.
for i in range(6):
    random.shuffle(monty_hall)
    #The user enters their 1st choice
    choice = input("Choose from doors 1, 2, and 3... : ")
    #A door that has a goat is revealed, cannot be the one user chose
    reveal = list(monty_hall)               #makes a duplicate list to avoid messing up the original
    reveal[int(choice) - 1] = '-'           #removes user's choice so that it won't be opened, but keeps in the element to not mess up the indices
    print("Monty opens door " + str(reveal.index('G') + 1) + " to reveal a goat!")
    #The user is prompted to choose again
    choice = input("Re-enter your choice. You have the option to switch to the other door.\n> ")
    print("You got... ")
    #The prize behind the user's ultimate choice is revealed!
    if(monty_hall[int(choice) - 1] == 'C'):
        print("a car! Congratulations!")
    else:
        print("a goat! Better luck next time!")
        
    input("Type anything to play again\n> ")
