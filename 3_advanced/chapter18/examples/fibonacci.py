def fibonacci(n):

    # n is the position of the number in the sequence. So fibonacci(5) means we
    # are finding the 5th fibonacci number going from the left

    if n < 0:
        return "does not exist"
    elif n == 1:  # first number is 0
        return 0
    elif n == 2:  # second number is 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
