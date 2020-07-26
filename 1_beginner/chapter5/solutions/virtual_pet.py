"""
Virtual Pet
Code a virtual pet!
First, create three variables:  name, hunger, and happiness.
Initialize hunger to 6 and happiness to 0, and set name
to whatever you like. (e.g. 'Otto')

Your program should continuously take input from the user:
    If the user enters 'feed', decrease hunger by 2. Increase by 1 otherwise.
    If the user enters 'pet', increase happiness by 2. Decrease by 1 otherwise.
    If the user enters 'quit', end the program.

Your program should also print the status of your pet each time
it prompts the user to enter a command:
    Print "[pet name] is hungry" when hunger is above 5, where [pet name]
        is the name variable.
    Print "[pet name] wants more attention" when happiness is below 5.
    Print "[pet name] feels happy" when hunger is equal to or less than 5,
        and happiness is equal to or greater than 5.

Feel free to customize your virtual pet by changing the how much the hunger
and happiness variables increase and decrease, or add more actions!
"""

name = "Otto"
hunger = 6
happiness = 0

command = input("> ")
while command != "quit":  # Exits loop when user quits
    # change Otto's hunger or happiness based on user command
    if command == "feed":
        hunger -= 2  # Otto is fed, hunger decreases
        happiness -= 1  # Otto is not pet, happiness decreases
    elif command == "pet":
        happiness += 2  # Otto is pet, happiness increases
        hunger += 1  # Otto is not fed, hunger increases

    # display Otto's status
    if hunger > 5:  # Otto is not fed enough
        print(name + " is hungry")
    if happiness < 5:  # Otto is not pet enough
        print(name + " wants more attention")
    elif hunger <= 5 and happiness >= 5:  # Otto is satisfied!
        print(name + " feels happy")

    command = input("> ")  # Keep taking user input until user quits
