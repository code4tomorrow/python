# Check Key/Value Membership in a Dictionary

contacts = {'Daisy Johnson': '2468 Park Ave', 'Leo Fitz': '1258 Monkey Dr'}

if "Daisy Johnson" in contacts:
    print("Daisy Johnson is a key in contacts")
else:
    print("Daisy Johnson is not a key in contacts")

if "1234 Main St" in contacts.values():
    print("1234 Main St is a value in contacts")
else:
    print("1234 Main St is not a value in contacts")
