# Reset the moving rectangle's position if it leaves the screen!
# The rectangle that will be moving is already provided
# it is `red_rectangle`. Your job is to move it across the screen
# at a speed of 5px down and 5px right per frame. Then, if the
# bottom of the rectangle is greater than the screen height or the
# right of the rectangle is greater than the screen width, reset
# the rectangle's x and y to 0 and 0.

import pygame

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Reset Position")

# color constants
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# makes a pygame.Rect rectangle
# the syntax is `myvar = pygame.Rect(top-left x, top-left y, width, height)`
red_rectangle = pygame.Rect(0, 0, 100, 100)

# add code here
