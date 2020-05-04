# Dictionaries

print(">>>Why should you use dictionaries?")

# implementation 1 using if statements
value = 10
if value == 10:
   print("Tom")
elif value == 20:
   print("Daniel")
elif value == 30:
   print("Elizabeth")

# implementation 2 using dictionary
dict1 = {10: "Tom", 20: "Daniel" , 30: "Elizabeth" }
print(dict1[value])

print()

print(">>> Initializing dictionaries")
contacts = {
    "John Doe": "1234 Main St",
    "Jane Smith": "5678 Market St",
    "Daisy Johnson": "1357 Wall St"
}
print(contacts)

print()

# retrieving, updating, and adding values
print(">>> Retrieving, updating, and adding values")

daisy_address = contacts["Daisy Johnson"]
print(daisy_address) # prints “1357 Wall St”

contacts["Daisy Johnson"] = "2468 Park Ave"
print(contacts["Daisy Johnson"]) # prints “2468 Park Ave”

contacts["Leo Fitz"] = "1258 Monkey Dr"
print(contacts) # prints the dictionary with the new entry

print()

# manipulating dictionaries
print(">>> Manipulating dictionaries")

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
print(coulson_address) # prints -1

# pop - removes the value at a specified key and returns
# the removed value
removed_address = contacts.pop("John Doe")
print(removed_address) # prints "1234 Main St"
print(contacts) # John Doe has been removed

# del - deletes a dictionary or key-value pair
del contacts["Jane Smith"] # deletes Jane Smith

# this would delete the entire dictionary:
# del contacts

# copy - returns a copy of the dictionary
copy_of_contacts = contacts.copy()
print(copy_of_contacts)

# clear - removes all key-value pairs from the dictionary
contacts.clear()
print(contacts)

print()

# iterating through dictionaries
print(">>> Iterating through dictionaries")

contacts = copy_of_contacts # undo the clear

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

print()

# checking if a key or value is in a dictionary
print(">>> Checking if a key or value is in a dictionary")

if "Daisy Johnson" in contacts:
    print("Daisy Johnson is a key in contacts")
else:
    print("Daisy Johnson is not a key in contacts")

if "1234 Main St" in contacts.values():
    print("1234 Main St is a value in contacts")
else:
    print("1234 Main St is not a value in contacts")