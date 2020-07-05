# Check Key/Value Membership in a Dictionary

contacts = {
    "John Doe": "1234 Main St",
    "Jane Smith": "5678 Market St",
    "Daisy Johnson": "1357 Wall St"
}

if "Daisy Johnson" in contacts:
    print("Daisy Johnson is a key in contacts")
else:
    print("Daisy Johnson is not a key in contacts")

if "1234 Main St" in contacts.values():
    print("1234 Main St is a value in contacts")
else:
    print("1234 Main St is not a value in contacts")
