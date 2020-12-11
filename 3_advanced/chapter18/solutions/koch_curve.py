"""
This is a fun problem that uses the turtle module.
If you’ve never used the turtle module, the first two
lines below are how to set it up and lines after are basic instructions:

import turtle
bob = turtle.Turtle() #doesn’t have to be bob
bob.left(angle) #turns bob left to an angle like 90
bob.right(angle) #turns bob right to an angle like 90
bob.fd(distance) #moves bob forward “distance” amount
# Depending on what IDE you are using, you may have to use bob.mainloop() if a window with an arrow doesn’t pop up.

The goal of this problem is to create a koch curve.
[search up what koch curve looks like]

A koch curve works as follows:
-Draw a Koch curve with length x/3.
-Turn left 60 degrees.
-Draw a Koch curve with length x/3.
-Turn right 120 degrees.
-Draw a Koch curve with length x/3.
-Turn left 60 degrees.
-Draw a Koch curve with length x/3.
However, if x<3, you will just move bob(the turtle) forward by length x

Credits to:
http://greenteapress.com/thinkpython2/html/thinkpython2006.html
"""

import turtle

bob = turtle.Turtle()


def kochcurve(x):
    if x < 3:
        bob.fd(x)
    else:
        kochcurve(x / 3)
        bob.left(60)
        kochcurve(x / 3)
        bob.right(120)
        kochcurve(x / 3)
        bob.left(60)
        kochcurve(x / 3)


kochcurve(90)  # doesn't to be 90, could be any number
