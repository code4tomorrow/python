# initializing a tuple
mytuple = () # is an empty tuple
myothtuple = (1,) # if you only have one element, you need the comma to keep it as a tuple
mylasttuple = (4,6,3,{5,6]) # it's a valid tuple; tuples accept all types

# modifying a tuple
# you can't modify a tuple's main elements
anothtuple = (4,56,7,[4,6,8])
# what won't work:  anothtuple[2] = 3   
# will produce an error
# what will work:
anothtuple[3][0]=6 
# this works since you aren't modifying the tuple's elements; you're modifying the list's elements

# tuple methods
# includes .index and .count
lasttupexample = (4,6,8,10, 4, 2)
print(lasttupexample.count(4)) # prints 2 since there are two 4's
print(lasttupexample.index(4)) # works just like indexes in lists; prints 0, the first occurence
