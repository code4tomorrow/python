"""
Integer

Write a program that takes any number
(decimals included) as input, and outputs
whether or not it's an integer.
"""

# Get input as a floating point
x = float(input("Enter a number: "))

# Compare x to the integer version of itself
is_integer = x == int(x)

print("Is integer? " + str(is_integer))
