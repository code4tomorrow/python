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

import pygame
import time  # not necessary, but used for frame cap

pygame.init()  # initialize pygame module

SCREEN_SIZE = (600, 400)
RECT_SIZE = (100, 100)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
momentum = [1, 1]  # (down and right)

window = pygame.display.set_mode(SCREEN_SIZE)
running = True

# start the rectangle in the middle of the screen
x = SCREEN_SIZE[0] // 2
y = SCREEN_SIZE[1] // 2

while running:
    # if the rectangle collided with the left or right side
    # of the screen
    if x + RECT_SIZE[0] >= SCREEN_SIZE[0] or x <= 0:
        momentum[0] = -momentum[0]
    # if the rectangle collided with the top or bottom
    # of the screen
    if y + RECT_SIZE[1] >= SCREEN_SIZE[1] or y <= 0:
        momentum[1] = -momentum[1]

    # add the speed to the current x and y to get the
    # new x and y
    x += momentum[0]
    y += momentum[1]

    window.fill(BLACK)  # 'erase' the previous frame
    pygame.draw.rect(window, RED, (x, y, RECT_SIZE[0], RECT_SIZE[1]))
    pygame.display.update()  # update the display

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    time.sleep(0.01)  # frame cap to make the rectangle more visible

pygame.quit()  # deactivate the pygame module
