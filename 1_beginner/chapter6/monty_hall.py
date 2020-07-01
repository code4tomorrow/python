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
#Make the Monty Hall game repeat 6 times.

#Make a list that represents the three closed doors, 'G' for the doors that have a goat, 'C' for the door that has a car.
#This step has already been done for you.
import random
monty_hall = ['G', 'G', 'C']

random.shuffle(monty_hall) #The shuffle function from the random module randomizes the doors every loop

#The user enters their 1st choice.

#A door that has a goat is revealed, cannot be the one user chose

#The user is prompted to choose again

#The prize behind the user's ultimate choice is revealed!
