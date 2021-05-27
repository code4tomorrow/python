class dot_example:  # use 'class' keyword followed by your class' name
    # classes can store functions and data; we call functions "methods"
    # we call data "attributes"

    # below are dot_example's attributes
    fun = True
    difficult = False


our_example = dot_example()  # instantiate the class; make sure to use ()

# would print True
print(our_example.fun)  # our_example is the object, fun is the attribute

# would print False
print(
    our_example.difficult
)  # our_example is the object, difficult is the attribute
