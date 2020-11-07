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

    """
        Elementwise power: raises each element in our vector to the given power
        """

    def __pow__(self, power):
        return Vector([i ** power for i in self.vals])

    """
        Addition: adds each element to corresponding element in other vector
        """

    def __add__(self, vec):
        return Vector(
            [self.vals[i] + vec.vals[i] for i in range(len(self.vals))]
        )

    """
        Multiplies each element in the vector by a specified constant
        """

    def __mul__(self, constant):
        return Vector([self.vals[i] * constant for i in range(len(self.vals))])

    """
        Elementwise subtraction: does the same as addition, just subtraction instead
        """

    def __sub__(self, vec):
        return self + (vec * (-1))


vec = Vector([2, 3, 2])
otherVec = Vector([3, 4, 5])
print(str(vec))  # [2, 3, 2]
print(vec ** 2)  # [4, 9, 4]
print(vec - otherVec)  # [-1, -1, -3]
print(vec + otherVec)  # [5,  7, 7]
print(vec * 5)  # [10, 15, 10]
