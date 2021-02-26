"""
Implement the less than and greater than operators for
the Matrix class(from a previous example problem) so that
we compare them based on their Frobenius norms which we
have implemented in the earlier section as an exercise.
Also, the unmodified Matrix class code will be given.
"""

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

# write your code below
