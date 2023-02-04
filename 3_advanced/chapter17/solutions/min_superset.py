# Given 3 sets of distinct integers, return the size of the superset
# of minimum size which is the superset of all the given sets.
# Implement the following method:


# superset calcuated using Principle of Inclusion and Exclusion
# sets: a vector containing 3 sets
def findMinSupersetLength(sets):
    total = 0
    for i in range(3):
        total += len(sets[i])
    for i in range(3):
        prevIndex = ((i - 1) + 3) % 3
        nextIndex = (i + 1) % 3
        total -= len(sets[prevIndex].intersection(sets[nextIndex]))
    total += len(sets[0].intersection(sets[1]).intersection(sets[2]))
    return total


sets = [{1, 2, 3}, {2, 3, 5}, {1, 3, 6}]

print(findMinSupersetLength(sets))


"""
Alternate, more understandable solution:
def findMinSupersetLength(sets):
    a = sets[0]
    a = a.union(sets[1]).union(set[2])
    return len(a)
"""
