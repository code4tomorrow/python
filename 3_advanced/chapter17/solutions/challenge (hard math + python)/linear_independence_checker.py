def calculateDeterminant(matrix):
  length = len(matrix)
  if length == 2:
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
  cofactorLength = length - 1
  total = 0
  negativeFactor = 1
  for i in range(length):
    matrixMinor = [[0 for k in range(cofactorLength)] for j in range(cofactorLength)]
    for j in range(cofactorLength):
      for k in range(cofactorLength):
        if k >= i: matrixMinor[j][k] = matrix[j+1][k+1]
        else: matrixMinor[j][k] = matrix[j+1][k]
    total = total + negativeFactor * matrix[0][i] * calculateDeterminant(matrixMinor)
    negativeFactor *= -1
  return total

def testLinearIndependence(mat):
  return calculateDeterminant(mat) != 0

mat = [
  [1, 1, 4],
  [0, 0, 5],
  [0, 7, 8]
]

print(testLinearIndependence(mat)) # prints True (determinant is equal to -35)
