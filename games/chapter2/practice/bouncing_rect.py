# Make a “bouncing rectangle!”

# For this, please use the given screen and rectangle
# width and height.

# The rectangle should start in (or close to) the middle of the 
# screen. It should be moving down and right. If it collides
# with the screen’s lower or upper boundary, it should reverse
# its vertical direction. If it collides with the screen’s left
# or right boundary, it should reverse its horizontal direction.

# Note: you can import the time module as well and use 
# time.sleep(0.01)
# in your mainloop to act as a frame cap to make your rectangle
# more visible

# put imports here

SCREEN_SIZE = (600, 400)
RECT_SIZE = (100, 100)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
momentum = [1, 1]  # (down and right)
