"""
Let's see the difference between linear and binary searches!
Some of the algorithm is already done for you, but you
will have to fill in some areas.

Then, run the code and you can see the results
"""

import random
from datetime import datetime as d


def linear_search(arr, val) -> int:
    """
    Linear Search - iterates through all the items in the array and checks
    equality with the provided value. If the value matches, returns
    the index of that value. Else, returns -1
    Arguments:
        arr - the array to search
        val - the value to search for
    Returns:
        int - index of the value on success, -1 on failure
    """
    for i in range(len(arr)):
        # your code here
        pass
    return -1


def binary_search(arr, val) -> int:
    """
    Binary Search - checks the list for a value using a binary search.
    Only works on sorted lists since it assumes that all the values
    in indexes greater than i are greater and all the values in
    indexes less than i are less.
    Arguments:
        arr - the array to search
        val - the value to search for
    Returns:
        int - index of the value on success, -1 on failure
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        current = (low + high) // 2
        if val == arr[current]:
            # your code here
            pass
        elif val < arr[current]:
            # your code here
            pass
        else:  # val > arr[current]
            # your code here
            pass
    return -1


# example 1 - sorted list
# the below demonstrates the binary search is faster than
# linear search on sorted lists
size = 100000
lst_1 = [i for i in range(size)]

tests = 3
for i in range(tests):
    print(f"sorted test #{i+1}:")
    print("searching linearly")
    target = random.randint(0, size)
    linear_start = d.now()
    linear_result = linear_search(lst_1, target)
    linear_end = d.now()
    print(
        "finished searching linearly in "
        + f"{(linear_end - linear_start).total_seconds()} seconds "
        + f"and got the {'right' if linear_result == target else 'wrong'} result"
        + f" ({linear_result})"
    )

    print("searching binarily")
    binary_start = d.now()
    binary_result = binary_search(lst_1, target)
    binary_end = d.now()
    print(
        "finished searching binarily in "
        + f"{(binary_end - binary_start).total_seconds()} seconds "
        + f"and got the {'right' if binary_result == target else 'wrong'} result"
        + f" ({binary_result})"
    )
    print()

# example 2 - unsorted list
# the below demonstrates that binary search doesn't work on unsorted
# lists, but linear search does
size = 100000
lst_2 = [i for i in range(size)]
random.shuffle(lst_2)

tests = 3
for i in range(tests):
    print(f"unsorted test #{i+1}:")
    print("searching linearly")
    idx = random.randint(0, size)
    target = lst_2[idx]
    linear_start = d.now()
    linear_result = linear_search(lst_2, target)
    linear_end = d.now()
    print(
        "finished searching linearly in "
        + f"{(linear_end - linear_start).total_seconds()} seconds "
        + f"and got the {'right' if linear_result == idx else 'wrong'} result"
        + f" ({linear_result})"
    )

    print("searching binarily")
    binary_start = d.now()
    binary_result = binary_search(lst_2, target)
    binary_end = d.now()
    print(
        "finished searching binarily in "
        + f"{(binary_end - binary_start).total_seconds()} seconds "
        + f"and got the {'right' if binary_result == idx else 'wrong'} result"
        + f" ({binary_result})"
    )
    print()
