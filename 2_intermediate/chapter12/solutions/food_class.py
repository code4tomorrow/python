"""
Food

Create a Food class with 4 instance
attributes: name. calories, grams of
protein, and grams of fat.

It should have 2 methods: an eat method
that prints "You are eating " and the name
of the food, and a burn method that prints
"You burned [x] calories." where [x] is
the number of calories in the food.

Create a JunkFood subclass and a Meal
subclass. Both subclasses should carry
over the attributes and methods of the
Food class.
The JunkFood subclass should have an
additional attribute for the grams of
sugar contained in the food, and the Meal
subclass should have an additional attribute
for the mg of sodium it contains.

Create a list called snacks and fill it with at
least 3 junk foods, and create a list called
meals and fill it with at least 3 meals.
Then, use Python to show that you ate all the
foods in both lists, and burned off one meal
(pick this meal randomly).
Display the total number of calories,
grams of protein, grams of fat, grams of
sugar, and mg of sodium that you ate (the total
for all the foods in both lists).
"""
import random


class Food:
    def __init__(self, name, cals, protein, fat):
        self.name = name
        self.cals = cals
        self.protein = protein
        self.fat = fat

    def eat(self):
        print("You are eating " + self.name + ".")

    def burn(self):
        print("You burned %d calories." % self.cals)


class JunkFood(Food):
    def __init__(self, name, cals, protein, fat, sugar):
        super().__init__(name, cals, protein, fat)
        self.sugar = sugar


class Meal(Food):
    def __init__(self, name, cals, protein, fat, sodium):
        super().__init__(name, cals, protein, fat)
        self.sodium = sodium


snacks = [
    JunkFood("Oreo", 55, 0.5, 2.2, 4.1),
    JunkFood("Brownie", 70, 2, 3, 2),
    JunkFood("Chips", 160, 2, 10, 0),
]

meals = [
    Meal("Rice and beans", 400, 10, 5, 15),
    Meal("Burrito", 350, 8, 9, 100),
    Meal("Pizza", 500, 20, 15, 150),
]

cals, protein, fat, sugar, sodium = 0, 0, 0, 0, 0

for snack in snacks:
    snack.eat()
    cals += snack.cals
    protein += snack.protein
    fat += snack.fat
    sugar += snack.sugar

for meal in meals:
    meal.eat()
    cals += meal.cals
    protein += meal.protein
    fat += meal.fat
    sodium += meal.sodium

# Choose a random meal to burn off.
meals[random.randrange(len(meals))].burn()

# Display totals
print("Totals eaten:")
print("Calories:", cals)
print("Protein (g):", protein)
print("Fat (g):", fat)
print("Sugar (g):", sugar)
print("Sodium (mg):", sodium)
