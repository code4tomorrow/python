# Libraries

# import the random module
import random

# returns a random number between 1 and 10 (exclusive)
number = random.randrange(1, 10)
print(number)

# import the entire module
# import module_name

# import the module and refer to it as a different name in your code 
# (typically a shortened name)
# this is called aliasing a module
# import module_name as shortened_name

# from a certain module, import only a certain class, variable, or method
# from module_name import thing_in_module

# wildcard (*) import - imports everything in that module
# from module_name import *