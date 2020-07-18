# Write a function that takes in 3 integers. Get the sum of the 3 integers. Get
# the difference between the largest integer and the smallest integer. The
# function will return the product of these two integers you got.
#
# Use this function on 1,2,3 and print it. Use this function on 5,13,7 and
# print it


def num_mystery(first_int, second_int, third_int):
    sum_of_three = first_int + second_int + third_int
    largest = max(first_int, second_int, third_int)
    smallest = min(first_int, second_int, third_int)
    diff_ls = largest - smallest

    return sum_of_three * diff_ls


print(num_mystery(1, 2, 3))  # should print 12
print(num_mystery(5, 13, 7))  # should print 200
