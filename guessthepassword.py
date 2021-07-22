# Directions: The goal of this exercise is to create
# a game where the user has to guess a certain password that
# you set and see how many tries it takes for that user to guess correctly

# start with assigning the password to some variable
pas = str("password")

# set an input so it will appear in the console and ask the user
guess = input("Enter the password:")

# set a counter to count the number of guesses
counter = 1

# set a while loop to check if the user guess correctly and count the number of guesses
while guess != pas:
    guess = input("Incorrect Password. Try Again:")
    counter += 1

# print the results
print(f"Nice Job. Unlocked. It took you {str(counter)} tries")
