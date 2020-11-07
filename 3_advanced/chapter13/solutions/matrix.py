"""
Build a class called Matrix which will take a list of lists
(containing integers) and store it as a field. Add an assertion
using the keyword assert to ensure that the list of lists is
rectangular (i.e. assert len(list_0) = len(list_i) for i in range(n))
You should also implement a __str__ method so that we can print
the contents of the matrix using print without having to access its field.
"""

# write your code below

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
 
mymatrix=Matrix([[3,4],[7,8],[4,8]])
print(str(mymatrix))
