"""
Integer Info
Create a program that takes an integer as input and
creates a list with the following elements:
    The number of digits
    The last digit
    A 'True' boolean value if the number is even, 'False' if odd
Print the list.
Some examples are given to help check your work.
"""

# Example 1: The input 123456 should print [6, 6, True]
# Example 2: The input 101202303 should print [9, 3, False]

num = int(input("Enter an integer: "))  # convert string input to int
info = [
    len(str(num)),
    num % 10,  # mod 10 of any number will return its last digit
    num % 2 == 0
]
print(info)
