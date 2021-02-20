# Create a database to store orders. Next, ask the customer for their
# name and store that as a variable. Next, ask the customer whether
# they want to view their previous order or make a new order.

# If they want to make a new order, use the shelf to store the order
# as the value and the customer’s name as the key.

# If they want to view a previous order, check if their name is in
# the shelf’s keys. If it is, print their previous order.
# If not, tell them that they haven’t ordered.
# Remember to close the shelf.
# Hint: to store their order, you can do: shelf[name] = order

import shelve
shelf = shelve.open("orders")
name = input("What is your name? ")
instruction = input("Would you like to view a previous order or make" +
  " a new order?\nAnswer with 'order' or 'view': ")
if instruction == "order":
  order = input("Type any order: ")
  shelf[name] = order
elif instruction == "view" and name in shelf.keys():
  print("Here is your previous order: ")
  print(shelf[name])
elif instruction == "view" and name not in shelf.keys():
  print("Sorry, you don't seem to have ordered before.")
shelf.close()
