# In linear algebra, a vector (list) of  n vectors (lists) each
# containing n integers are considered linearly independent if we
# solve the following equation
# a * x   +  a * x   +  a * x  +  a * x  = 0
#  1   1      2   2      3   3     n   n
# for where they can be any real constant, and we find that all of
# them equal to 0 being the only possible solution for this system
# of equations (this is called the trivial solution). Write a method
# which takes a vector of n vectors each of size n and determine if
# they are linearly independent. Return true if linearly independent,
# and false otherwise.
# (for this question, assume n is less than equal to 4 and greater than 1)

# Note: Another way we can determine if n vectors is linearly independent is if
# you find that the matrix formed by concatenating the vectors has a nonzero
# determinant. This might be somewhat easier
# (search up calculating “determinant using cofactor expansion”).


def calculateDeterminant(matrix):
    length = len(matrix)
    if length == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    cofactorLength = length - 1
    total = 0
    negativeFactor = 1
    for i in range(length):
        matrixMinor = [
            [0 for k in range(cofactorLength)] for j in range(cofactorLength)
        ]
        for j in range(cofactorLength):
            for k in range(cofactorLength):
                if k >= i:
                    matrixMinor[j][k] = matrix[j + 1][k + 1]
                else:
                    matrixMinor[j][k] = matrix[j + 1][k]
        total = total + negativeFactor * matrix[0][i] * calculateDeterminant(
            matrixMinor
        )
        negativeFactor *= -1
    return total


def testLinearIndependence(mat):
    return calculateDeterminant(mat) != 0


mat = [[1, 1, 4], [0, 0, 5], [0, 7, 8]]

print(testLinearIndependence(mat))  # prints True (determinant is equal to -35)
