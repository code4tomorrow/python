# Given two sets of integers A and B (each element in these sets are
# between 1 and 1000 inclusive), find the similarity of the two sets
# (the sets are guaranteed to be nonempty). The similarity is a number
# which is computed by dividing the size of the intersection of the
# two sets by their union size.
# Note: the intersection is the # of elements that both sets have in common.


def computeSimilarity(set1, set2):
    intersectionSize = 0
    for elem in set1:
        if elem in set2:
            intersectionSize += 1
    unionSize = len(set1) + len(set2) - intersectionSize
    return intersectionSize / float(unionSize)


print(computeSimilarity({1, 2}, {1, 3}))
