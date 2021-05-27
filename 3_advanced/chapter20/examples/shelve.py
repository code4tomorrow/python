# shelve is a Python module that aids with storing data.
# It functions similar to a dictionary, although it
# only allows keys to be strings.


import shelve

"""this will create a database if you don’t already have one and open it if you do"""

myshelf = shelve.open("mydatabase")

myshelf["key1"] = 4

# remember, while the key must be a string, the value can be any type

print(myshelf["key1"])  # will give me 4

myshelf.close()
