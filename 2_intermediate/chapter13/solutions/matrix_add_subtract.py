"""
Write a modified version of the Matrix class(that was defined in
one of the example problems in this section) with an __add__
operation as well as a __sub__ operation. It should add matrices,
assuming that they will be of the same length. Also, the unmodified
Matrix class code will be given.
"""

# write your code below


"""
This is the unmodified Matrix class code.

class Matrix:
   def __init__(self,thelist: list):
       self.thelist=thelist
       for items in range(len(self.thelist)):
           assert type(self.thelist[items]) == list
           assert len(self.thelist[0]) == len(self.thelist[items])
           for things in range(len(self.thelist[items])):
               assert type(self.thelist[items][things]) == int

   def __str__(self):
       return str(self.thelist)
"""


class Matrix:
    def __init__(self, thelist: list):
        self.thelist = thelist
        for items in range(len(self.thelist)):
            assert type(self.thelist[items]) == list
            assert len(self.thelist[0]) == len(self.thelist[items])
            for things in range(len(self.thelist[items])):
                assert type(self.thelist[items][things]) == int

    def __str__(self):
        return str(self.thelist)

    def __add__(self, other):
        assert type(other) == Matrix
        for items in range(len(self.thelist)):
            for things in range(len(self.thelist[items])):
                self.thelist[items][things] += other.thelist[items][things]

    def __sub__(self, other):
        assert type(other) == Matrix
        for items in range(len(self.thelist)):
            for things in range(len(self.thelist[items])):
                self.thelist[items][things] -= other.thelist[items][things]


mymatrix = Matrix([[3, 4], [7, 8]])
othermatrix = Matrix([[5, 6], [7, 8]])
mymatrix - othermatrix
print(mymatrix.thelist)
