# Code to figure out how many of a factor a number has


def number_factor(number, factor, factor_counter=0):
    """
    Parameters:
    1) number is the number in which we are finding the number of
    factors of. EX: 24
    2) factor is the factor in which we are finding the number of
    in the parameter number. EX: 2
    Output: The number of times the parameter number can be divisible
    by the parameter factor. This number is also the parameter
    factor_counter right before it is returned. EX: 3
    """

    if number % factor != 0:  # Base Case
        return factor_counter
    else:  # Recursive Case
        return number_factor(number / factor, factor, factor_counter + 1)


print(number_factor(24, 2))


def countdown(n, arr=[]):
    if n < 0:  # base case 1
        return "out of bounds"
    if n == 0:  # base case 2
        return arr
    # recursive case
    arr.append(n)
    return countdown(n - 1, arr)


print(countdown(5))
