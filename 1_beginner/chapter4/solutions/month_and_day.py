"""
Write a program that takes user input of the month and date,
and prints out "Boo!" if it is Halloween, and "April fools!"
if it is April fools' day. If it is any other month and date,
print "It's not Halloween or April Fools..."
Assume all inputs are integers (for example, month 1 is January).
"""

# ask user for month and date
month = int(input("Enter a month: "))
day = int(input("Enter a date: "))

# print a message based on the month and date
if month == 10 and day == 31:
    print("Boo!")
elif month == 4 and day == 1:
    print("April fools!")
else:
    print("It's not Halloween or April Fools...")
