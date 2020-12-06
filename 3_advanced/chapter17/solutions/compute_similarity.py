def computeSimilarity(set1, set2):
  intersectionSize = 0
  for elem in set1:
    if elem in set2:
      intersectionSize += 1
  unionSize = len(set1) + len(set2) - intersectionSize
  return intersectionSize / float(unionSize)

print(computeSimilarity({1, 2}, {1, 3}))
