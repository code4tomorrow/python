# Iterating Through Dictionaries

contacts = {
    "John Doe": "1234 Main St",
    "Jane Smith": "5678 Market St",
    "Daisy Johnson": "1357 Wall St"
}

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
