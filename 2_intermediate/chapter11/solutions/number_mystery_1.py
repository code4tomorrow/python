# Number Mystery 1
# Write a function called num_mystery that takes in 3 integers.
# The function should calculate the sum of the 3 integers and
# the difference between the largest integer and the smallest integer.
# The function should return the product of these two integers you calculated.
#
# Hint: You may find it useful to use the max() and min() functions.
#
# Use the num_mystery function on 1, 2, 3 and print the result.
# Use the num_mystery function on 5, 13, 7 and print the result.


def num_mystery(first_int, second_int, third_int):
    # calculate the sum of the 3 numbers
    sum_of_three = first_int + second_int + third_int

    # calculate the difference between the max and min
    largest = max(first_int, second_int, third_int)
    smallest = min(first_int, second_int, third_int)
    difference = largest - smallest

    # return the product
    return sum_of_three * difference


print(num_mystery(1, 2, 3))  # prints 12
print(num_mystery(5, 13, 7))  # prints 200
