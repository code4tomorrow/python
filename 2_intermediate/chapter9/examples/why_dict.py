# Why Dictionaries

# dictionaries as an alternative to parallel lists
names = [
    "Jane Doe",
    "John Williams",
]
addresses = ["1234 Main St", "5678 Market Pl", "1357 Wall St"]

# better solution: make a dictionary to
# explicitly associate a name with an address
# this is also called mapping a key to a value
contacts = {
    "Jane Doe": "1234 Main St",
    "John Williams": "5678 Market Pl",
    "Alex Summers": "1357 Wall St",
}

# implementation 1 using if statements
value = 10
if value == 10:
    print("Tom")
elif value == 20:
    print("Daniel")
elif value == 30:
    print("Elizabeth")

# implementation 2 using dictionary
dict1 = {10: "Tom", 20: "Daniel", 30: "Elizabeth"}
print(dict1[value])
