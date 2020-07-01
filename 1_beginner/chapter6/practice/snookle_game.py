"""
Snookle Game
Snookle the sheep wants to play a game.
Given a list of positive integers and a main number, the player iterates
through each element in the list and chooses to either add it or
to subtract it from the current main number.

This is done by having the user enter either 'add' or 'subtract' every turn.
The main number will be updated to the new value.

A player wins if they make 12 to be the main number.
If the end of the list is reached, go back to the first element
in the list and keep going until the player wins.
Code the game for Snookle!
"""

# example values to get you started
nums = [3, 1, 4, 2, 6, 5, 8, 10]
main = 7
