import shelve
total = 0
ashelf = shelve.open("mydb")
for val in ashelf.values():
    if isinstance(val, int):
        total += val
print(total)
ashelf.close()
