"""
Catalog

Write a program that takes asks the
user whether they'd like to add, delete,
or clear the entries in a store catalog.

After they perform some action, the program
should display the updated dictionary in the
format:
    item1: price1
    item2: price2
    etc.

Keep asking them if they'd like to add, delete,
or clear entries until they enter "q".

Possible actions:
If they enter "add":
    Ask them to enter an item.
    Ask them to enter a price.
    The item should be the key, and the price
    should be the value in the dictionary.

If they enter "delete":
    Ask them to to enter which item
    they'd like to delete.

If they enter "clear":
    Clear all the entries from the dictionary.

If they enter "q":
    Display the final dictionary and end the program.
"""

catalog = {}

while True:
    # Display catalog
    print("Current catalog:")
    if len(catalog) != 0:
        for item, price in catalog.items():
            print(item + ": $" + price)
    else:
        print("Your catalog is empty.")
    print()

    ans = input(
        "Would you like to add, delete, "
        "or clear entries from your catalog? "
    )

    # Perform actions depending on input
    if ans == "q":
        break
    elif ans == "add":
        item = input("Enter an item to add: ")
        price = input("Enter the price: $")
        catalog[item] = price
    elif ans == "delete":
        item = input("Enter an item to delete: ")
        del catalog[item]
    elif ans == "clear":
        catalog.clear()
    print()
