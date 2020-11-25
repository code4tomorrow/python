def logarithm(number, base=10, at=1, times=0):
  if number<1 or base==1: return None
  if number==1: return 0 
  if at>number: return times-1
  if at==number: return times
  newcurrent = at * base
  return logarithm(number,base,newcurrent,times+1)
