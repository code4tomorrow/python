"""
Write a class called PolarCoordinates which will take a
value called radius and angle. When we print this class,
we want the coordinates in Cartesian coordinates, or we want
you to print two values: x and y. (If you don’t know the
conversion formula, x = radius * cos(angle), y = radius * sin(angle).
Use Python’s built-in math library for the cosine and sine operators)
"""

# write your code below

import math


class PolarCoordinates:
    def __init__(self, radius, angle):
        self.radius = radius
        self.angle = angle

    def __str__(self):
        self.x = self.radius * math.cos(self.angle)
        self.y = self.radius * math.sin(self.angle)
        return "{},{}".format(self.x, self.y)


group = PolarCoordinates(2, math.pi)
print(str(group))
