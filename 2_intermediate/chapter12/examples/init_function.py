class Tesla:
    def __init__(self, maxSpeed=120, color="red"):
        # the init function always needs the self keyword
        # if no maxSpeed is entered, maxSpeed will default to 120
        # if no color is entered, color will default to "red"

        # set the class' attribute maxSpeed to the provided maxSpeed
        self.maxSpeed = maxSpeed

        # set the class' attribute color to the provided color
        self.color = color


p1 = Tesla(140, "blue")
print(p1.maxSpeed)  # will print 140
print(p1.color)  # will print "blue"
