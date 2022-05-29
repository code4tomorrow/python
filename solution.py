import pygame

pygame.init() # initializes pygame module

SCREEN_SIZE = (800,800)
BLACK = (0, 0, 0)  # background color
BLUE = (0, 0, 255) # color of font
WHITE = (255,255,255) # color of rectangle
momentum = (2,2)

window = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Moving-Text")


# make a pygame.Rect rectangle
white_rectangle = pygame.Rect(0, 100, 130, 40)

# move the text with coordinates instead of the rectangle
x = 0 # x-coordinate of the top-left pixel of text
y = 400 # y-coordinate of the top-left pixel of text

# sets a font and font size
font = pygame.font.SysFont("Times New Roman", 40)

# create a piece of text
text = font.render("HELLO", False, BLUE)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # moves a pygame.Rect rectangle relative to its position
    white_rectangle.move_ip(momentum)  # moves 2 to the right, 2 down

    # move the text by coordinates
    x += 1 # move right by one pixel
    y += 1 # move down by one pixel

    # erase the previous frame
    window.fill(BLACK)

    # draw a rectangle that is a pygame.Rect object
    pygame.draw.rect(window, WHITE, white_rectangle)

    # draws text onto the rectangle
    window.blit(text, white_rectangle)
    # you can also use coordinates in the form of a tuple
    # the coordinates would place the top left pixel
    # Syntax: window.blit(text, (x,y))

    # update the screen
    pygame.display.update()

    syntax: pygame.time.wait(30) # adds a 30 millisecond delay

pygame.quit()  # close pygame after finishing