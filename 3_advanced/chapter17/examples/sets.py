# initialize a set with the following syntax
myset = {"item 1", "item 2", "any type besides list and dict", 5, 8, 3}
# or
myothset = set()  # creates an empty set
notaset = {}  # doesn't create a set; creates a dict; remember that

# sets don't always print the same way
# try it
print(myset)
print(myset)
print(myset)
# for this reason, indexing won't work with sets
# try it
anotherset = {"this", "might", "not", "be", "in", "order"}
for i in anotherset:
    print(i)

# subsets and supersets
# a superset is a set that has all the items that a subset has
oursuperset = {1, 3, 5, 7, 9}
oursubset = {1, 5, 3}

# should print True since oursuperset has 1,5, and 3
print(oursuperset.issuperset(oursubset))
# should print True since oursuperset has 1,5, and 3
print(oursubset.issubset(oursuperset))
# should print False since oursubset doesn't have 7 or 9
print(oursubset.issuperset(oursuperset))

# set methods
# includes .intersection , .union , .difference , .symettricdifference
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# will print 3,4,5 which is the common items (the 'intersection')
print(set1.intersection(set2))
# will print 1,2 which is the different items in set 1 (the 'difference')
print(set1.difference(set2))
# will print 6,7 which is the difference items in set 2 (the 'difference')
print(set2.difference(set1))
# will print 1,2,6,7 since those are the different items in both
print(set1.symettricdifference(set2))
# will print 1,2,3,4,5,6,7 since those are the unique items
print(set1.union(set2))

# set methods (cont.)
# also includes .add , .discard , .remove , .pop , .update
# note: .discard and .remove are similar; check the comments
a_set = set()
a_set.add(2)  # can only add 1 element
a_set.update([8, 9, 7])  # is a union between a_set and {8,9,7}
a_set.remove(8)  # removes 8; if 8 isn't there, raises a key error
a_set.discard(9)  # removes 9; if 9 isn't there, do nothing (no error)
a_set.pop()  # removes the first element; in this case 2
