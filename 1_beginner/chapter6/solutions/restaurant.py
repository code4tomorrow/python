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

foods = ["pancakes", "waffles", "toast"]
food_costs = [5, 3, 100]

drinks = ["juice", "water", "tea"]
drink_costs = [2, 50, 1]

sugar_foods = ["muffin", "lollipop", "brownie"]
sugar_costs = [4, 20, 15]

"""
2. Display the menu.
Iterate through the items and costs for each
category to do this.
"""

print("Welcome to my restaurant! Here's the menu:")
print("Foods:")
for i in range(len(foods)):
    print(foods[i] + ": $" + str(food_costs[i]))
print()

print("Drinks:")
for i in range(len(drinks)):
    print(drinks[i] + ": $" + str(drink_costs[i]))
print()

print("Sugar:")
for i in range(len(sugar_foods)):
    print(sugar_foods[i] + ": $" + str(sugar_costs[i]))
print()

print("Order in all lowercase!\n")

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

4. Finalize the total.
Add a 7% sales tax to your sum, and
round this value to 2 decimal places.
Display the total.

5. As mentioned in Step 3, ask the user if they want
to order again. If they say "no", then stop the program.
Otherwise, let them order again.
"""

# Take the user's order.
while True:
    cost = 0

    # Foods
    food = input("What food would you like? ")

    if food in foods:
        cost += food_costs[foods.index(food)]
    else:
        print("You didn't order a proper food... Adding $1000 to tab.")
        cost += 1000

    # Drinks
    drink = input("What drink would you like? ")

    if drink in drinks:
        cost += drink_costs[drinks.index(drink)]
    else:
        print("You didn't order a proper drink... Adding $1000 to tab.")
        cost += 1000

    # Sugar
    sugar = input("What sugar item would you like? ")

    if sugar in sugar_foods:
        cost += sugar_costs[sugar_foods.index(sugar)]
    else:
        print("You didn't order a proper sugary item! Adding $1000 to tab.")
        cost += 1000

    # Sales tax
    cost *= 1.07

    # Display output
    print("Your total is $%.2f." % cost)
    print()

    # Ask if the user wants to order again
    ans = input("Do you want to order again (\"yes\" or \"no\")? ")
    print()
    if ans == "no":
        break
