# Create a class called CountableSet which stores the number of times each
# element has been inserted into the CountableSet object.
# (Basically, store it like element: #of times inserted into Countable Set)
# Implement the following class:


class CountableSet:
    def __init__(
        self, objs
    ):  # objs is the initial list of objects to be inserted
        self.elems = {}
        for obj in objs:
            self.insert(obj)

    # insert x into the set one time, increment the count by one
    # returns True if map didn't already contain the key
    # x is the integer to be inserted
    def insert(self, x):
        if x in self.elems.keys():
            self.elems[x] += 1
            return False
        else:
            self.elems[x] = 1
            return True

    # decrement the count by one, returns True if map contains key
    # x is integer to be deleted
    def delete(self, x):
        if x in self.elems.keys():
            self.elems[x] -= 1
            if self.elems[x] == 0:
                self.elems.pop(x)
            return True
        return False

    # returns the number of times x has been inserted into the set
    # x is the integer being queried
    def get(self, x):
        if x in self.elems.keys():
            return self.elems[x]
        return 0


x = CountableSet([1, 2, 3, 1])
x.insert(3)
print(x.elems)
x.insert(2)
print(x.elems)
x.delete(1)
print(x.elems)
x.delete(1)
print(x.elems)
