def listsum(arr):
  total = 0

  for i in arr:
    if type(i) == type([]):
      total = total + listsum(i)
    else:
      total = total + i

  return total
