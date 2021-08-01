# Build off of your previous code (the code from QuitPygameProblem.py)
# Draw the provided rectangle onto the screen.
# Move the object up when either the W or up arrow key is pressed;
# right when either the D or right arrow is pressed; etc.

import pygame

pygame.init()

run = True
width = 500
height = 500
white = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
screen.fill(white)

# rect[0] = rect color
# rect[1] = x-coord
# rect[2] = y-coord
# rect[3] = width
# rect[4] = height
rectangle = [(255, 0, 0), 20, 20, 20, 20]

# pygame main loop
while run:
    pygame.time.delay(50)
    # clear the screen by filling it white
    screen.fill(white)
    # draw rect
    pygame.draw.rect(
        screen,
        rectangle[0],
        pygame.Rect(rectangle[1], rectangle[2], rectangle[3], rectangle[4]),
    )
    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # there are a couple of ways of stopping the pygame
            # loop. One way is to set run = false. Or you can
            # import sys and use sys.exit() to stop your program.
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        # get states of keys
        keysPressed = pygame.key.get_pressed()
        # recall that y coord decreases as you go up the window
        # the origin is at the top left corner
        if keysPressed[pygame.K_UP] or keysPressed[pygame.K_w]:
            rectangle[2] -= 5 if rectangle[2] >= 5 else 0
        elif keysPressed[pygame.K_s] or keysPressed[pygame.K_DOWN]:
            rectangle[2] += 5 if rectangle[2] <= 475 else 0
        elif keysPressed[pygame.K_d] or keysPressed[pygame.K_RIGHT]:
            rectangle[1] += 5 if rectangle[1] <= 475 else 0
        elif keysPressed[pygame.K_a] or keysPressed[pygame.K_LEFT]:
            rectangle[1] -= 5 if rectangle[1] >= 5 else 0
    pygame.display.update()
