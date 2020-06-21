# Hours 
# Write a program that asks the user 
# how many hours they spend on the internet 
# per day, and return if they’re addicted 
# or not based on the hours. (5 or more hours 
# is addicted, less is not).

# prompt user for hours spent on internet
hours = int(input("How many hours/day do you spend on the internet? "))

# display whether or not the user is addicted
if hours >= 5:
    print("You are addicted to the internet.")
else:
    print("You aren't addicted to the internet.")