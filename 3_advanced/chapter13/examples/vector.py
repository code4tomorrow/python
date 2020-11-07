class Vector:
    """
    Constructor

    self: a reference to the object we are creating
    vals: a list of integers which are the contents of our vector
    """

    def __init__(self, vals):
        self.vals = vals  # Notice! We are using the keyword self to create a field or property (for Javascript users)
        print("Assigned values ", vals, " to vector.")

    """
	String Function
 
	Converts the object to a string in readable format for programmers
	"""

    def __str__(self):
        return str(self.vals)  # Returns the contents of the vector


vec = Vector([2, 3, 2])
print(str(vec))  # [2, 3, 2]
