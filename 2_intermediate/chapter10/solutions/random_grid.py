"""
Random Grid

Create a 2D list with 4 rows and a randomly
determined number of columns. The column
number should be a random EVEN number between
2 and 16 (inclusive).

All the even column numbers (including 0) should
be filled with asterisks (*). The odd numbered
columns should be filled with underscores (_).

Display the grid at the end by printing out
elements individually: don't use print(list).
Assume that you don't know the size of the grid
beforehand. In other words, if you wanted to display
the 2D list without knowing the number of rows and
columns in it, how would you code this?

For example, a 4x6 grid would display this:
*_*_*_
*_*_*_
*_*_*_

This might be useful:
print("a")
print("a")
would display the "a"s with newlines:
a
a

print("a", end=" ")
print("a")
changes the end of the first "a" from a newline to a space.
The output is this:
a a

"""
import random

grid = []
cols = random.randint(1, 8) * 2

# Fill the grid 2D list.
for row in range(4):
    grid.append([])
    for col in range(cols):
        grid[row].append(
            "*" if (col % 2 == 0) else "_"
        )

# Display the grid without knowing the size beforehand.
for row in grid:
    for col in row:
        print(col, end="")
    print()
