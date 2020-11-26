"""
Problem Name: square_root_list
Take a user given list of numbers and make a list of all the
square roots of the numbers using list comprehension. Use a
list comprehension to solve it.
Hint: The square root of a number is the same as taking the one half
power of a number.
"""

# The given code takes an input and makes it a list of numbers.
# For example, entering “1 23 4” as the input will result in the list [1,23,4]
ex_list = input().split()
for idx in range(len(ex_list)):
    ex_list[idx] = int(ex_list[idx])

# write your code below
