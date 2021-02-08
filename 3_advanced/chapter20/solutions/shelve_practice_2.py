# Use mydb.db . Using it, first create a total variable. Then, add
# all of the shelve’s values to the total. Remember to check if
# the value is an integer before adding it to the total.
# After all, shelves can store all types.

import shelve

total = 0
ashelf = shelve.open("mydb")
for val in ashelf.values():
    if isinstance(val, int):
        total += val
print(total)
ashelf.close()
