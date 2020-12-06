def dup_detector(item: list):
  theset = set(item)
  if len(theset) < len(item):
    return True
  else:
    return False

print(dup_detector([5,4,3,2,2])) # should print True
