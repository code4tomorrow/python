"""
Write a program that takes an integer input,
and prints the square of that number if it is even,
and prints the number itself otherwise.
"""

# prompt user to enter an int
number = int(input("Enter an integer: "))

if number % 2 == 0:
    # if number is even, print its square
    print(number ** 2)
else:
    # otherwise, print the number itself
    print(number)
