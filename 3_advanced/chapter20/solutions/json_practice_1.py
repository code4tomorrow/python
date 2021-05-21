# use the "favorite_foods.json"
# in that json file, there will be a dictionary called "favorite_foods"
# print all the unique favorite foods, which will be the values.
# Save all the names into a list. Add that list to the dictionary
# ('names' should be the key and the names list should be the value)
# and write the dictionary into the json file

import json

a = open("favorite_foods.json", "r")
x = json.load(a)
names = []
foods = set()
for name, food in x["favorite foods"].items():
    foods.add(food)
    names.append(name)
for food in foods:
    print(food)
x["names"] = names  # create an item within the dictionary that has the names
a.close()
n = open("favorite_foods.json", "w")
json.dump(x, n, indent=4)
n.close()
