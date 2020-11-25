import turtle
bob = turtle.Turtle()

def kochcurve(x):
  if x<3: bob.fd(x)
  else:
    kochcurve(x/3)
    bob.left(60)
    kochcurve(x/3)
    bob.right(120)
    kochcurve(x/3)
    bob.left(60)
    kochcurve(x/3)

kochcurve(90)  # doesn't to be 90, could be any number
