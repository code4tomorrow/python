# Fibonacci
# The Fibonacci sequence starts with 0 and 1.
# The next number in the sequence is the sum of the previous 2 numbers.
# Thus, the first 5 Fibonacci numbers are: 0, 1, 1, 2, 3.


def recursive_fib(n):
    """
    Returns the nth number in the Fibonacci sequence recursively

    Args:
        n (int): the position of the number in the Fibonacci sequence you want

    Returns:
        int: the nth number in the Fibonacci sequence
        For example, recursive_fib(5) will return 3
    """
    if n <= 0:  # Base Case 1: out of bounds
        return None
    elif n == 1:  # Base Case 2
        return 0
    elif n == 2:  # Base Case 3
        return 1
    else:  # Recursive Case
        return recursive_fib(n - 1) + recursive_fib(n - 2)


def iterative_fib(n):
    """
    Returns the nth number in the Fibonacci sequence iteratively

    Args:
        n (int): the position of the number in the Fibonacci sequence you want

    Returns:
        int: the nth number in the Fibonacci sequence
        For example, iterative_fib(5) will return 3
    """
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        prev1 = 0  # fib(n - 2)
        prev2 = 1  # fib(n - 1)

        current = 0

        # Start at n = 3 because we already "handled" n = 1 and n = 2.
        # need n + 1 because range's end parameter is exclusive.
        # Alternatively, you can do: for i in range(2, n)
        for i in range(3, n + 1):
            current = prev1 + prev2

            prev1 = prev2
            prev2 = current

        return current


def fib_sequence(n):
    """
    Returns the fibonacci sequence as a list up to the nth fibonacci number

    Args:
        n (int): the position of the number in the Fibonacci
        sequence you want to go up to

    Returns:
        list: the nth number in the Fibonacci sequence
        For example, fib_sequence(5) will return [0, 1, 1, 2, 3]

    Adapted from: https://medium.com/@danfcorreia/fibonacci-iterative-28b042a3eec
    """
    sequence = [0, 1]

    for i in range(2, n):
        sequence.append(sequence[i - 2] + sequence[i - 1])

    return sequence


print("Recursive fib:", recursive_fib(5))
print("Iterative fib:", iterative_fib(5))
print("Fib sequence:", fib_sequence(5))
