# Create an empty set and print the type of it. Create a
# set from a given dictionary(do set(given_dict)) and print it.
# Note: The set created from the given dictionary contains
# only the keys of the dictionary.


def set_creator(given_dict):
    empty_set = set()
    print(type(empty_set))
    dict_set = set(given_dict)
    print(dict_set)


set_creator({1: "Wall Street", 2: "Main Street", "Tower": 3})
