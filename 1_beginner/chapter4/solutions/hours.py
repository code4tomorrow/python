# Hours
# Write a program that asks the user
# how many hours they spend on the internet
# per day, and print if they’re addicted
# or not based on the hours. (5 or more hours
# is addicted, less is not).

# prompt user for hours spent on internet
hours = int(input("How many hours/day do you spend on the internet? "))

# display whether or not the user is addicted
if hours >= 5:
    print("You are addicted to the internet.")
else:
    print("You aren't addicted to the internet.")


# See if you can write the same program,
# except that the user is addicted to the internet
# if the number of hours they spend on the internet
# is greater than 2 times the remainder of hours / 7

hours = int(input("How many hours/day do you spend on the internet? "))
if hours > 2 * (hours % 7):
    print("You are addicted to the internet.")
else:
    print("You aren't addicted to the internet.")
