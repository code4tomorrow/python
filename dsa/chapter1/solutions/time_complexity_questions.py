"""
Classify the following code examples with their
runtimes. Write your responses as comments.
"""


def do_something():
    # runtime for do_something() is O(1)
    pass


# what is the runtime for example 1?
# runtime is O(n)
def example_one(n):
    for i in range(n):
        do_something()


# what is the runtime for example 2?
# runtime is O(1)
def example_two(n):
    do_something()


# what is the runtime for example 3?
# runtime is O(n^2)
def example_three(n):
    for i in range(n):
        for x in range(i):
            do_something()


# what is the runtime for example 4?
# runtime is O(n)
def example_four(n):
    for i in range(n // 2):
        do_something()


# what is the runtime for example 5?
# runtime is O(log(n))
def example_five(n):
    i = 0
    while i < n:
        do_something()
        i *= 2


# what is the runtime for example 6?
# runtime is O(1)
def example_six(n):
    for i in range(10):
        do_something()


# what is the runtime for example 7?
# runtime is O(2**n)
def example_seven(n):
    for i in range(2**n):
        do_something()


# what is the runtime for example 8?
# runtime is O(n)
def example_eight(n):
    for i in range(n):
        for x in range(7):
            do_something()


# what is the runtime for example 9?
# runtime is O(n^2)
def example_nine(n):
    for i in range(n):
        example_one(n)


# what is the runtime for example 10?
# runtime is O(n)
def example_ten(n):
    i = 0
    while i < n:
        do_something()
        i += 2
