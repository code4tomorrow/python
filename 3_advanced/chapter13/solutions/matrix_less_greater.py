"""
Implement the less than and greater than operators for
the Matrix class(from a previous example problem) so that
we compare them based on their Frobenius norms which we
have implemented in the earlier section as an exercise.
Also, the unmodified Matrix class code will be given.
"""

# write your code below

import math

"""
This is the unmodified Matrix class code.

class Matrix:
 def __init__(self,thelist: list):
   self.thelist=thelist
   for items in range(len(self.thelist)):
     assert type(self.thelist[items])==list
     assert len(self.thelist[0]) == len(self.thelist[items])
     for things in range(len(self.thelist[items])):
       assert type(self.thelist[items][things])==int

 def __str__(self):
   return str(self.thelist)
"""


class Matrix:
    def __init__(self, thelist: list):
        self.thelist = thelist
        self.norm = 0
        for items in range(len(self.thelist)):
            assert type(self.thelist[items]) == list
            assert len(self.thelist[0]) == len(self.thelist[items])
            for things in range(len(self.thelist[items])):
                assert type(self.thelist[items][things]) == int

    def froebiannorm(self):
        self.squared = 0
        for items in range(len(self.thelist)):
            for things in range(len(self.thelist[items])):
                self.squared += self.thelist[items][things] ** 2
        self.norm = math.sqrt(self.squared)

    def __str__(self):
        return str(self.norm)

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

    def __lt__(self, other):
        assert type(other) == Matrix
        return self.norm < other.norm

    def __gt__(self, other):
        assert type(other) == Matrix
        return self.norm > other.norm


mymatrix = Matrix([[3, 4], [7, 8]])
othermatrix = Matrix([[5, 6], [7, 8]])
print(mymatrix > othermatrix)
