class Vector:
    """
    Constructor

    self: a reference to the object we are creating
    vals: a list of integers which are the contents of our vector
    """

    def __init__(self, vals):
        self.vals = vals
        # print("Assigned values ", vals, " to vector.")

    """
    String Function

    Converts the object to a string in readable format for programmers
    """

    def __str__(self):
        return str(self.vals)

    def __pow__(self, power):
        return Vector([i ** power for i in self.vals])

    # Calculates Euclidean norm
    def norm(self):
        return sum((self ** 2).vals) ** 0.5

    # __lt__:  implements the less than operator (<)
    def __lt__(self, other):
        return self.norm() < other.norm()

    # __gt__: implements the greater than operator (>)
    def __gt__(self, other):
        return self.norm() > other.norm()

    # __le__: implements the less than equal to operator (<=)
    def __le__(self, other):
        return self.norm() <= other.norm()

    # __ge__: implements the greater than equal to operator (>=)
    def __ge__(self, other):
        return self.norm() >= other.norm()

    # __eq__: implements the equals operator (==)
    def __eq__(self, other):
        return self.norm() == other.norm()

    # __ne__:implements the not equals operator (!=)
    def __ne__(self, other):
        return self.norm() != other.norm()


vec = Vector([2, 3, 2])
vec2 = Vector([3, 4, 5])
print(vec < vec2)  # True
print(vec > vec2)  # False

print(vec <= vec2)  # True
print(vec >= vec2)  # False
print(vec <= vec)  # True
print(vec >= vec)  # True

print(vec == vec2)  # False
print(vec == vec)  # True

print(vec != vec2)  # True
print(vec != vec)  # False
