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


# See if you can write the same program, but they are addicted on if the number they input (x) is great than two times 
#the remainder of that number when divided by 7 (remainder when x is deivided by 7)

hours = int(input("How many hours/day do you spend on the internet? "))
if hours >= 2*(hours%7):
    print("You are addicted to the internet.")
else:
    print("You aren't addicted to the internet.")