# Create a recursive sequence that finds the sum of
# a list that may contain another list within it.
#
# Solution Visualizer URL: https://www.w3resource.com/python-exercises/
# data-structures-and-algorithms/python-recursion-exercise-3.php

def listsum(arr):
    total = 0

    for i in arr:
        if isinstance(i, list):
            total = total + listsum(i)
        else:
            total = total + i

    return total
