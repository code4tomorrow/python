class Tesla:
    def __init__(self, maxSpeed=120, color="red"):
        self.maxSpeed = maxSpeed
        self.color = color

    # a method; acts just like a function, but needs self keyword
    def drive(self):
        print("The car is now driving")


p1 = Tesla(140, "blue")
p1.drive()  # will print "The car is now driving"
