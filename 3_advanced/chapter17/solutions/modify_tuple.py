# Given a tuple whose first two elements are
# strings and the third element is a dictionary.
# Add the given key and value to the dictionary
# in the tuple.


def modify_tuple(given_tuple, given_key, given_val):
    given_tuple[2][given_key] = given_val


given_tuple = ("Ken", "Kaneki", {1: "Apple"})
modify_tuple(given_tuple, 2, "Orange")
print(given_tuple)  # Dictionary should now be updated
