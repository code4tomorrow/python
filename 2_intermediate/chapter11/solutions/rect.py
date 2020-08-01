"""
Rect

Write a function that takes in 2 integer
parameters: length, and width.

The function should print out a rectangle of
asterisks (*) with that length and width.

Example, if the length is 5 and the width is 3,
the function should print:
*****
*****
*****

Useful information:
1)  print("a", end="")
    removes the newline from the end of the print statement.
2)  print("a" * 5) displays "aaaaa".

Use the function to display rectangles with
the following dimensions (with a linebreak
between each one):
2x6
7x4
3x5

"""


# Define a function with length and width parameters.
def draw_rect(length, width):
    for row in range(width):
        print("*" * length)
    print()


# Use the function to draw rectangles of various sizes.
draw_rect(2, 6)
draw_rect(7, 4)
draw_rect(3, 5)
