# shelve is a Python module that aids with storing data.
# It functions similar to a dictionary, although it
# only allows keys to be strings.


import shelve

# this will open or create a database
myshelf = shelve.open("mydatabase")

# remember, while the key must be a string, the value can be any type
myshelf["key1"] = 4

print(myshelf["key1"])  # prints 4

myshelf.close()
# always remember to close the shelve after writing to save the data
