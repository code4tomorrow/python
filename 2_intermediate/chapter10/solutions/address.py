"""
Address

Create a 2D list where each row represents a
person and has 3 elements: their name, their age,
and their address.

The entire list should have 4 such entries (4 people),
so it will be a 4x3 list.

Display the name and address of the 2nd person in the list.

Then, display the entire list with the format:
name (age): address
"""

contacts = [
    ["Jeremy", 10, "45 Pancake Road"],
    ["Nicey", 18, "111 Cupcake Street"],
    ["Hawthorne", 15, "19 Sinister Avenue"],
    ["Nilah", 14, "Banks of the Nile River"]
]

# 2nd person
print(contacts[1][0] + ": " + contacts[1][2])
print()

# Display the entire list.
for contact in contacts:
    print(
        contact[0] + " (%d): " % contact[1] + contact[2]
    )
