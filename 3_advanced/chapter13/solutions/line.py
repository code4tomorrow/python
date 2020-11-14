"""
Write a class called Line which will take the arguments slope
and intercept in its constructor. When we print the class,
the __str__ method should return a string with the line expressed
in the form  “y=mx+b” where m and b are the slope and intercept
respectively.
"""

# write your code below


class Line:
    def __init__(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept

    def __str__(self):
        self.equation = "y={}x+{}".format(self.slope, self.intercept)
        return self.equation


myline = Line(3, 1)
print(str(myline))
