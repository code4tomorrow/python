"""
Restaurant
Write a program that asks someone
what they want to order and give them
the total cost of their meal.

Each meal should have 3 categories
(ex. food, drinks, desserts), and the user
must order 1 item from each category.

Make sure to include a 7% sales tax
(multiply the total by 1.07), and
round the answer to 2 decimal places

The steps are outlined in the following code.
"""

"""
1. Store the menu in lists.
Each of the 3 categories should have an
items menu and a costs menu.

Example of the 6 lists you need to create:
foods, food_costs, drinks, drink_costs,
desserts, dessert_costs
"""

# Insert your lists here.

"""
2. Display the menu.
Iterate through the items and costs for each
category to do this.

Example output:
Welcome to my restaurant! Here's the menu:

Food:
Pancakes: $5
Waffles: $3
Toast: $100

Drinks:
Juice: $2
Water: $50
Tea: $1

Sugar:
Muffin: $4
Lollipop: $20
Brownie: $15
"""

# Insert the code for displaying the menu here.

"""
3. Ask the user to order.
This code should be in a loop. After you display the
user's total at the end, ask them if they want to
order again. If they say "no", the program should end.
Otherwise, you should take their order and display the
new total again.

As you take their order, check if what they ordered
is in the corresponding list for that category.
If it is, add the price of the item to the total.
Otherwise, display a warning message and add $1000 to the total.

Example order (using menu above):
What food would you like? pancakes
What drink would you like? water
What sugar item would you like? candy
You didn't order a proper sugary item! Adding $1000 to tab.
"""

# Insert the code that takes the user's order here.
# Make sure it's in a loop.

"""
4. Finalize the total.
Add a 7% sales tax to your sum, and
round this value to 2 decimal places.
Display the total.
"""

# Add the code to finalize and display the total here.

"""
5. As mentioned in Step 3, ask the user if they want
to order again. If they say "no", then stop the program.
Otherwise, let them order again.
"""

# Ask the user if they want to order again here.
