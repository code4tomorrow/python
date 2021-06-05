# The self keyword is used when you want a method or
# attribute to be for a specific object. This means that,
# down below, each Tesla object can have different maxSpeed
# and colors from each other.


class Tesla:
    def __init__(self, maxSpeed=120, color="red"):
        self.maxSpeed = maxSpeed
        self.color = color

    def change(self, c):
        self.color = c


p1 = Tesla(140, "blue")
p2 = Tesla(100, "blue")


# Notice how, when we use the self keyword, each object can
# have different attributes even though they are from the
# same class.

p1.change("green")
print(p1.color)  # prints "green"

p2.change("yellow")
print(p2.color)  # prints "yellow"
