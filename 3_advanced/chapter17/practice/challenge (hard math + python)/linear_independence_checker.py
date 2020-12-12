"""

In linear algebra, a vector (list) of  n vectors (lists) each containing n integers are considered linearly independent if we solve the following equation
a * x   +  a * x   +  a * x  +  a * x  = 0
 1   1      2   2      3   3     n   n

for  where they can be any real constant, and we find that all of them equal to 0 being the only possible solution for this system of equations 
(this is called the trivial solution). Write a method which takes a vector of n vectors each of size n and determine if 
they are linearly independent. Return true if linearly independent, and false otherwise. 
(for this question, assume n is less than equal to 4 and greater than 1)

Note: Another way we can determine if n vectors is linearly independent is if you find that the matrix formed by
concatenating the vectors has a nonzero determinant. This might be somewhat easier (search up calculating “determinant using cofactor expansion”).
"""

def calculatedeterminant(matrix):
  # put your code here; remove "pass"
  pass
  
def linearindependence(mat)
  return calculatedeterminant != 0
 
# mat is an example of an acceptable list of 3 (n) lists each containing 3 (n) integers
# hint: if you use mat, it should give you True
mat = [
  [1,1,4],
  [0,0,5],
  [0,7,8]
]
