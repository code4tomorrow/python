""" Writing """
import json
x = open('filename.json', 'w')
topdict = {}

chinese = {
 "hello": "ni hao",
 "bye": "zai jian",
 "how are you": "ni hao ma"
}
frenchlist = [34, 1, 2, 6]

topdict["chinese"] = chinese
topdict["frenchlist"] = frenchlist
json.dump(topdict, x, indent=4)
x.close()


""" Reading """
import json
x = open('./testit.json', 'r')
y = json.load(x)
# assuming that testit.json had been written to
for key in y:
    print(key, ", ", y[key])
x.close()


""" Editing a pre-existing JSON file """
import json
x = open('filename.json', 'r')
y = json.load(x)  # y becomes the equivalent of a "top_dict"
x.close()
# the value can be all the normal types that dictionaries can hold
y["some_key"] = "some value"
x = open("filename.json", "w")
json.dump(y, x, indent=4)
x.close()


""" json.dumps() method """
import json
oldDict = {"fname": "john", "lname": "doe", "age": 20}
print("oldDict:", type(oldDict))  # prints data type of oldDict
newStr = json.dumps(oldDict)  # converts oldDict to string format
print("newStr:", type(newStr))  # prints data type of newStr


""" json.loads() method """
import json
oldStr = '{"fname": "john", "lname": "doe", "age": 20}'
print("oldStr:", type(oldStr))  # prints data type of oldStr
newDict = json.loads(oldStr)  # converts oldStr to string format
print("newDict:", type(newDict))  # prints data type of newDict
