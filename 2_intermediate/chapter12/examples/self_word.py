class Tesla:
    def __init__(self, maxSpeed=120, color="red"):
	self.maxSpeed = maxSpeed
	self.color = color

    def change(self, c):
        self.color = c


p1 = Tesla(140, "blue")

p1.change("yellow")
print(p1.color)  # prints "yellow"
p1.color = "hello"
print(p1.color)  # prints "hello"
