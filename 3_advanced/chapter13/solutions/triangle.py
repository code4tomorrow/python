"""
Write a class called Triangle which will take three tuples
(each tuple contains two integers: the x and y coordinates
of a vertex). Then, define an __add__ operation that acts as
a translation operation. Its input argument will be a tuple
of two integers that will indicate the x and y translations
that will be applied to each coordinate. (basically, add the
tuple to each coordinate of the triangle). Also, define a
vertical and horizontal transformation tool in the form
of __mul__ which will also take a tuple of two integers that
will be multiplied to the x and y coordinates of each vertex
respectively.
"""

# write your code below

class Triangle:
 def __init__(self, pair1, pair2, pair3):
   self.coordinatelist = [pair1,pair2,pair3]
   for i in range(len(self.coordinatelist)):
     assert type(self.coordinatelist[i])==tuple and len(self.coordinatelist[i])==2
     self.coordinatelist[i] = list(self.coordinatelist[i])
 
 def __add__(self,other):
   assert type(other)==tuple and len(other)==2
   for i in range(len(self.coordinatelist)):
     self.coordinatelist[i][0] += other[0]
     self.coordinatelist[i][1] += other[1]
   return tuple(self.coordinatelist)
 
 def __mul__(self,other):
   assert type(other)==tuple and len(other)==2
   for i in range(len(self.coordinatelist)):
     self.coordinatelist[i][0] *= other[0]
     self.coordinatelist[i][1] *= other[1]
   return tuple(self.coordinatelist)
 
mytriangle=Triangle((0,0),(1,0),(0,1))
print(mytriangle + (1,1))
print(mytriangle * (2,2))
