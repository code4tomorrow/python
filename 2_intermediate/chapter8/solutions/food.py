"""
Food
Start with an empty list called food.
Ask the user to either enter a fruit, a vegetable,
or a junk food item. Do this 10 times, and each time,
the question you ask should be selected randomly.

Add each of their answers to the list, sort the list
alphabetically, and then display the final list
by printing each item on a separate line.
"""
import random

foods = []
prompts = [
    "Enter a fruit: ",
    "Enter a vegetable: ",
    "Enter a junk food item: ",
]

# Choose a random prompt and collect input.
for i in range(10):
    i = random.randrange(len(prompts))
    item = input(prompts[i])
    foods.append(item)
print()

foods.sort()
for food in foods:
    print(food)
