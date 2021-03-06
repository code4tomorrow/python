# use the file "wildlife.json"
# load the data in the JSON file
# add at least one habitat and corresponding animal(s) to the dictionary
# finally, write the updated dictionary to the json file.

import json

a = open("wildlife.json", "r")
x = json.load(a)
a.close()
x["Deepest Peru"] = "Paddington"
n=open("wildlife.json", "w")
json.dump(x, n, indent=4)
n.close()
