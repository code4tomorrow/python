# notice how there is no base
# case, meaning no way out

def recurse(i):
	i = i + 1
	print(i)
	recurse(i) 

recurse(0)
