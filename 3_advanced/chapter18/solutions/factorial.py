# Create a recursive method that mirrors how a
# factorial would work in math.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
