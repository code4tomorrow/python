# Fred had lost his teddy bear, so his parents are going to the store
# to buy a replacement for him. You are given a list of length 2
# (2 elements) tuples, where each tuple represents a teddy bear. where
# the first element contains a number showing how similar that that bear is
# to Fred's original teddy bear(the smaller, the better), and the second
# element is a string of the teddy bear's name.
# Find the teddy bear closest to the one Fred lost, and print its name
# (don’t worry about tuples w/ same #)


def tuple_bears(item):
    ourmin = [item[0][0], item[0][1]]
    for i in range(len(item)):
        if ourmin[0] > item[i][0]:
            ourmin[0] = item[i][0]
            ourmin[1] = item[i][1]
            i = 0
    return ourmin[1]


tuplelist = [(5, "Freddy"), (3, "Runaway"), (7, "Killer"), (2, "Luscious")]

print(tuple_bears(tuplelist))
