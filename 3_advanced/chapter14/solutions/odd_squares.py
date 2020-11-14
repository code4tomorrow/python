# Problem name: odd_squares
# Given a list of integers, create a list of all the squares of the odd
# integers within the list.
# Use a list comprehension to solve it.

# the given code takes an input and makes it a list of numbers
# for example, entering “1 23 4” as the input will result in the list [1,23,4]
ex_list = input().split()
for idx in range(len(ex_list)):
    ex_list[idx] = int(ex_list[idx])

# write your code below
odds_quares = [n ** 2 for n in list if n % 2 == 1]
