"""
A restaurant menu has food and drink sections,
each from which the customer must choose an order.
By default, any combination of food and drink orders
are $1,000,000,000.

But if the customer enters 'french toast'
AND 'coffee', there is a discount of $1.

Otherwise, if the customer enters 'chicken soup' OR 'apple juice',
the price increases by $1.

Write a program that takes an order from a user
and prints out the appropriate price.
Assume that all inputs are in lowercase
and that it is always food first, and then drink.
"""

# all orders are $1 million by default
total_cost = 1_000_000_000  # underscores to increase readability

# take the user's order
food = input("What food would you like? ")
drink = input("What drink would you like? ")

# discount of $1 if the user orders french toast and coffee
if food == "french toast" and drink == "coffee":
    total_cost -= 1
# charge extra $1 if user orders chicken soup or apple juice
elif food == "chicken soup" or drink == "apple juice":
    total_cost += 1

# display total
print("Total cost: $" + str(total_cost))
