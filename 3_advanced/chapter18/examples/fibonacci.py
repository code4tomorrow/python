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
        return None  # base case; out of bounds

    current = 0
    next_term = 1

    for i in range(n - 1):  # this is equivalent to for i in range(1, n)
        current, next_term = next_term, current + next_term
        # this is just a slightly rewritten fib sequence;
        # instead of looking at the past 2 cases, it looks at the
        # current and next terms to determine the next next term

    return current  # will be 0 if n is 1, 1 if n is 2, etc...


def fib_sequence(n):
    """
    Returns the fibonacci sequence as a list up to the nth fibonacci number

    Args:
        n (int): the position of the number in the Fibonacci
        sequence you want to go up to

    Returns:
        list: the nth number in the Fibonacci sequence
        For example, fib_sequence(5) will return [0, 1, 1, 2, 3]

    Adapted from:
    https://medium.com/@danfcorreia/fibonacci-iterative-28b042a3eec
    """
    sequence = [0, 1]

    for i in range(2, n):
        sequence.append(sequence[i - 2] + sequence[i - 1])

    return sequence


print("Recursive fib:", recursive_fib(5))
print("Iterative fib:", iterative_fib(5))
print("Fib sequence:", fib_sequence(5))
