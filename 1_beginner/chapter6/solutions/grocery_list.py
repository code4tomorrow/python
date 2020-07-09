"""
Grocery List

Create a program that prompts the
user to continuously enter items for a grocery
list. Stop asking them for items
when the user enters 'quit'.

Print the grocery list in a numbered format.

Ask the user to enter prices for each
item in the grocery list in order.

Finally, ask the user how many of
each item they bought. Based on their
input, calculate the total grocery bill
and display it. (Bonus points if you
can format the money so that it displays
2 decimals.)

Demo: https://youtu.be/BmMj16Ox5iA
"""

item = ""
items = []  # stores grocery items

# continuously ask user for grocery items
# and store them in a list
while item != "quit":
    item = input("Enter a grocery item, or 'quit': ")
    if item != "quit":
        items.append(item)

# print items in numbered format
for i in range(0, len(items)):
    print(str(i + 1) + ". " + items[i])

print()

# ask user to enter prices for
# each grocery item
prices = []
for i in range(0, len(items)):
    price = float(input("Enter price for " + items[i] + ": $"))
    prices.append(price)

print()

# ask user for quantity of each
# item in the grocery list
quantities = []
for i in range(0, len(items)):
    quantity = int(input("Enter quantity bought for " + items[i] + ": "))
    quantities.append(quantity)

print()

# calculate total grocery bill
total = 0
for i in range(0, len(items)):
    total += prices[i] * quantities[i]

# print total, formatted to 2 decimals
# because it's money
print("Total: $%.2f" % total)
