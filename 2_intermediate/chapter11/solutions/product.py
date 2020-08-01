"""
Product

Write a function that takes a list
of numbers as input and returns
the product of all the numbers in
the list.

Use it to print the products of the
following sets of numbers:
-1, 5, 3, 2, 8
2.5, 3, 0
4, 3, 7, 10
"""


# Define a product() function with a list parameter.
def product(list):
    product = 1
    for i in list:
        product *= i
    return product


# Use the function to display products, where
# each set of numbers is given as a list.
print(product([-1, 5, 3, 2, 8]))
print(product([2.5, 3, 0]))
print(product([4, 3, 7, 10]))
