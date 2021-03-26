# Domestic bees make their honeycombs in rings where the total cells is
# (n + 1) * (3n) + 1  where n is the number of rows in the honeycomb
# Create a function that takes one argument and prints how many total
# cells there are in the honeycomb.
# If the argument is not the correct type, print a message saying so.
# It should be able to run through the list provided.


def type_checker(x):
    try:
        print((x + 1) * (3 * x) + 1)
        # note to students: print(x * any number) would not result in
        # an error if x is a string; it would just print x that many
        # times
    except TypeError:
        print("That's not a valid number")


arg_list = [4, "hi", "obviously NAN", 5.6]
for i in arg_list:
    type_checker(i)
