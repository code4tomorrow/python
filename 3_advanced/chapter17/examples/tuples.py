# initializing a tuple
mytuple = ()  # is an empty tuple
myothtuple = (1,)  # tuples with just 1 item need a comma at the end
moretuple = (4, 6, 3, {5, 6}, [7])  # valid; tuples accept all types

# modifying a tuple
# you can't modify a tuple's main elements
anothtuple = (4, 56, 7, [4, 6, 8])
# what won't work:  anothtuple[2] = 3
# will produce an error
# what will work:
anothtuple[3][0] = 6
# this works since you you're modifying the list's elements, not the tuple's

# tuple methods
# includes .index and .count
lasttupexample = (4, 6, 8, 10, 4, 2)
print(lasttupexample.count(4))  # prints 2 since there are two 4's
print(lasttupexample.index(4))
# ^works just like list indexes; prints 0 which = the first occurence
