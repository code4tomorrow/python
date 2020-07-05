# Manipulating Dictionaries

contacts = {
    "John Doe": "1234 Main St",
    "Jane Smith": "5678 Market St",
    "Daisy Johnson": "2468 Park Ave",
    "Leo Fitz": "1258 Monkey Dr"
}

# get - retrieves the value at a specified key
leo_address = contacts.get("Leo Fitz")
print(leo_address)

# the following gives you an error
# because "Melinda May" is not a key:
# melinda_address = contacts["Melinda May"]

# however, using the get(keyname, value) method,
# you can specify the value that is returned
# if the key doesn't exist in the dictionary
coulson_address = contacts.get("Phil Coulson", -1)
print(coulson_address)  # prints -1

# pop - removes the value at a specified key and returns
# the removed value
removed_address = contacts.pop("John Doe")
print(removed_address)  # prints "1234 Main St"
print(contacts)  # John Doe has been removed

# del - deletes a dictionary or key-value pair
del contacts["Jane Smith"]  # deletes Jane Smith

# this would delete the entire dictionary:
# del contacts

# copy - returns a copy of the dictionary
copy_of_contacts = contacts.copy()
print(copy_of_contacts)

# clear - removes all key-value pairs from the dictionary
contacts.clear()
print(contacts)
