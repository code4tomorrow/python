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

win = False  # The game keeps going until this variable is set to True

while not win:
    for num in nums:
        # prompt user to add or subtract current num
        print("main number is currently " + str(main))
        choice = input("[add] or [subtract] " + str(num) + "?\n> ")

        # update main value based on choice
        if choice == "add":
            main += num
        elif choice == "subtract":
            main -= num

        # If the main number if 12, the user has won!
        if main == 12:
            win = True  # Exit while loop and end game
            break  # Exit for loop

print("Congrats you won the game!")
