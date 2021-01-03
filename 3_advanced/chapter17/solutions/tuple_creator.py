# Create an empty tuple and print the type of it.
# Create a tuple from any one element and print the type of it.
# Create a tuple from a given dictionary and print it.
# Note: The tuple created from a dictionary will only contain
# the keys of the dictionary

def tuple_creator(given_dict):
    empty_tuple = ()
    print(type(empty_tuple))
    one_element_tuple = ("Blueberry",)
    print(type(one_element_tuple))
    dict_tuple = tuple(given_dict)
    print(dict_tuple)

tuple_creator({1:"Wall Street", 2: "Main Street", "Tower": 3})
