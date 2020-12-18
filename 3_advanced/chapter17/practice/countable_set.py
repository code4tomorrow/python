# Create a class called CountableSet which stores the number of times each 
# element has been inserted into the CountableSet object.
# (Basically, store it like element: #of times inserted into Countable Set)
# Implement the following class:


class CountableSet:
    def __init__(
        self, objs
    ):  # objs is the initial list of objects to be inserted
        pass

    # insert x into the set one time, increment the count by one
    # returns True if map didn't already contain the key
    # x is the integer to be inserted
    def insert(self, x):
        pass

    # decrement the count by one, returns True if map contains key
    # x is integer to be deleted
    def delete(self, x):
        pass

    # returns the number of times x has been inserted into the set
    # x is the integer being queried
    def get(self, x):
        pass
