import pygame  # imports the module

# RESIZABLE is only needed if you want a resizable window
from pygame.locals import RESIZABLE

# initializes imported pygame modules
pygame.init()

# creates resizable pygame window that is 500 pixels wide and 400 high
# sets the caption of the window to "My first pygame app!"
flag = RESIZABLE
window = pygame.display.set_mode((500, 400), flag)
pygame.display.set_caption("My first pygame app!")

# this is where the game loop begins
run = True
while run:
    for event in pygame.event.get():
        # checks if the close button is pressed
        # if so, exit the game loop
        if event.type == pygame.QUIT:
            run = False

# deactivates pygame modules, opposite of pygame.init()
pygame.quit()
