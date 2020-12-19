# Code for finding the nth term in the Fibonacci sequence


def fibonacci(n):


    # Parameter: n is the position of the number in the Fibonacci sequence.
    # Output: The nth number of the Fibonacci sequence will be outputted.

    # fibonacci(5) means we are finding the 5th fibonacci number
    # in the fiboacci sequence going from the left

    if n < 0:  # Base Case 1: out of bounds
        return "Does not exist"
    elif n == 1:  # Base Case 2: first number is 0
        return 0
    elif n == 2:  # Base Case 3: second number is 1
        return 1
    else:  # Recursive Case:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
