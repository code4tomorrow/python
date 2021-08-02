# Create a pygame window.
# Close the pygame window when either the quit event occurs
# or the escape key is pressed.
# Use the provided width and height. Fill the screen with white

import pygame

pygame.init()

run = True
width = 500
height = 500
white = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
screen.fill(white)

# pygame main loop
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # there are a couple of ways of stopping the pygame
            # loop. One way is to set run = false. Or you can
            # import sys and use sys.exit() to stop your program.
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    pygame.display.update()
