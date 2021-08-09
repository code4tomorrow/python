import pygame

RED = (255, 0, 0)
BLACK = (0, 0, 0)
x = y = 0
width = 100
height = 50

# initializes imported pygame modules
pygame.init()

# creates pygame window that is 500 pixels wide and 400 high
# sets the caption of the window to "My first pygame app!"
window = pygame.display.set_mode((500, 400))
pygame.display.set_caption("My first pygame app!")

# this is where the game loop begins
run = True
while run:
    # change the coordinates
    x, y = x + 1, y + 1

    # draw a black screen over the previous frame
    window.fill(BLACK)

    # draw a new rectangle and update the screen
    pygame.draw.rect(window, RED, (x, y, width, height))
    pygame.display.update()

    for event in pygame.event.get():
        # checks if the close button is pressed
        # if so, exit the game loop
        if event.type == pygame.QUIT:
            run = False

# deactivate pygame modules, opposite of pygame.init()
pygame.quit()
