def tuple_bear(item: list):
    ourmin = [item[0][0], item[0][1]]
    for i in range(len(item)):
        if ourmin[0] > item[i][0]:
            ourmin[0] = item[i][0]
            ourmin[1] = item[i][1]
            i = 0
    return ourmin[1]


tuplelist = [(5, "Freddy"), (3, "Runaway"), (7, "Killer"), (2, "Luscious")]

print(tuple_bear(tuplelist))
