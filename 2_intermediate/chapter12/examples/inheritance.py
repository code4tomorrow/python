# Inheritance in coding is when one "child" class receives
# all of the methods and attributes of another "parent" class


class Test:
    def __init__(self):
        self.x = 0

# class Derived_Test inherits from class Test
class Derived_Test(Test):
    def __init__(self):
        Test.__init__(self)  # do Test's __init__ method
        # Test's __init__ gives Derived_Test the attribute 'x'
        self.y = 1


b = Derived_Test()

# Derived_Test now has an attribute "x", even though
# it originally didn't
print(b.x, b.y)
