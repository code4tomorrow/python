# use the "favorite_foods.json"
# in that json file, there will be a dictionary called "favorite_foods"
# print all the unique favorite foods, which will be the values.
# Save all the names into a list. Add that list to the top dictionary and write 
# the top dictionary into the json file

import json
a = open("favorite_foods.json", "r")
x = json.load(a)
names = []
for name, food in x["favorite foods"].items():
  print(food)
  names.append(name)
x["names"] = names # create an item within the dictionary that has the names
a.close()
n = open("testit.json", "w")
json.dump(x, n, indent = 4)
n.close()
