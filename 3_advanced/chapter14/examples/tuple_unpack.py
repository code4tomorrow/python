# Extracting values from "countries"


""" Typical way to extract values """
countries = ("china", "mexico", "brazil", "USA")

a = countries[0]
b = countries[1]
c = countries[2]
d = countries[3]

print(a, b, c, d)  # prints "china mexico brazil USA"


""" Extracting values with tuple unpacking """
a, b, c, d = countries

print(a, b, c, d)  # prints "china mexico brazil USA"


""" Special feature for tuple unpacking """
# Using the * says that you want all values
# in the middle of the tuple to be put together
# in a list.
a, *b, c = countries

print(a, b, c)  # prints "china ["mexico", "brazil"] USA"
