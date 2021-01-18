# Create a function that takes one argument and prints arg * 4.
# If the argument is not the correct type, print a message saying so.
# It should be able to run through the list provided.


def type_checker(x):
    try:
        print(x * 4)
    except TypeError:
        print("That's not a valid number")


arg_list = [4, "hi", "obviously NAN", 5.6]
for i in arg_list:
    type_checker(i)
