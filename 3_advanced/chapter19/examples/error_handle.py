try:
    x = 1
    y = "hi"
    x + y
except TypeError:  # this will only run if there's a TypeError
    print("incorrect types, try again")
except NameError:  # this will only run if there's a NameError
    print("maybe you forgot to create that")
else:  # this will run if no error occurs
    print("everything good here!")
finally:
    # will run no matter what
    print("x is", x, "\ny is", y)


string = "goodbye"
assert string == "hello", "string is not hello"
print(string)  # this will not be run because assert raises an exception
