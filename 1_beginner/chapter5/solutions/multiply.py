"""
Multiply

Write a program that asks the user
for 10 integers, multiplies them all
together, and displays the product at
the end.

Use a for loop!
"""

# Initial value is 1
product = 1

# Ask the user for 10 numbers and multiply.
for i in range(10):
    product *= int(input("Enter a number: "))

print("The product is " + str(product))
