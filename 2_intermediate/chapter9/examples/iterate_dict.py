# Iterating Through Dictionaries

contacts = {"Daisy Johnson": "2468 Park Ave", "Leo Fitz": "1258 Monkey Dr"}

# iterate through each key
for name in contacts:
    print(name)

# or, use keys() method
for name in contacts.keys():
    print(name)

# using each key to print each value
for name in contacts:
    # prints each address associated with each name
    print(contacts[name])

# iterate through each value using values()
for address in contacts.values():
    print(address)

# iterate through keys and values using items()
for name, address in contacts.items():
    print(name + ", " + address)
