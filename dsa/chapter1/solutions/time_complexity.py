"""
For each of the following time complexities, create
a function that has that time complexity. The following solutions
are examples and not the only ways to have done this problem.
"""


# time complexity: O(1)
def double_my_number(number):
    x = number
    x *= 2
    return x


# time complexity: O(n)
def sum_till_n(n):
    total = 0
    for i in range(n):
        total += i

    return total


# time complexity: O(n^2)
def print_triangle(n):
    for row in range(n):
        for column in range(row):
            print("* ", end="")
        print()


# time complexity: O(log(n))
def sum_powers_of_two(max_number):
    power_of_two = 1
    total = 0

    while power_of_two < max_number:
        total += power_of_two
        power_of_two *= 2

    return total


# time complexity: O(n * log(n))
def sum_many_powers_of_two(number_of_times):
    total = 0
    for i in range(number_of_times):
        # since sum_powers_of_two is O(log(n))and this for loop is O(n),
        # the resulting time complexity is O(n * log(n))
        total += sum_powers_of_two(i)

    return total


# time complexity: O(2**n)
def get_binary_combinations(number_of_digits):
    """
    Gets the combinations of binary numbers with number_of_digits digits
    For example, get_binary_combinations(2) should give
    ["00", "01", "10", "11"].

    """
    cur_options = ["0", "1"]
    next_options = []

    operations = 0

    # In total, this is O(2**n). It may be a bit confusing, but
    # this is O(2**n) because of the fact that the current options
    # doubles each time we go through the for loop, so it has to
    # spend twice as long each time.
    for i in range(number_of_digits - 1):
        for option in cur_options:
            next_options.append(option + "0")
            next_options.append(option + "1")
            operations += 1
        cur_options = next_options
        next_options = []

    print(f"took {operations} operations")
    return cur_options


# for comparison, here's a very easy to understand
# function with O(2**n) runtime.
def regular_o_2_to_the_n(n):
    operations = 0
    for i in range(2**n):
        operations += 1
    print(f"took {operations} operations")


# if you actually don't believe that get_binary_combinations is O(2**n),
# try running the below.
# as you can see, they have similar operational cost,
# meaning that get_binary_combinations really is O(2**n)
# times = 20
# get_binary_combinations(times)
# regular_o_2_to_the_n(times)
