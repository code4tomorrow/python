import shelve
keylist = []
myshelf = shelve.open("mydatabase")
for key in myshelf.keys():
    keylist.append(key)
keylist.sort()
for key in keylist:
    print(myshelf[key])
myshelf.close()
