"""
Code a function named shopping that will print the number
of items that a customer would like to buy. It will take in
an unknown number of parameters, each representing
one item. After that, the function will ask the customer,
"Are you sure you would like to buy" and stating the number
of items the customer wants to purchase. Your function does not
need to respond to a yes/no answer from the user; it just
needs to print the output (the question).


===Example 1===
# Parameters: "soap", "brush", "comb"
# Output: "Are you sure you would like to buy 3 items?"

===Example 2===
# Parameters: "lotion", "shoes", "pencil", "crayon"
# Output: "Are you sure you would like to buy 4 items?"
"""


def shopping(*args):
    item_number = len(args)
    print("Are you sure you would like to buy", item_number, "items?")


shopping("soap", "brush", "comb")
