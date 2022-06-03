import pygame

pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Drawing and Moving Objects")


# make a rectangle without the pygame.Rect class
x = 0  # top-left x value
y = 0  # top-left y value
width = 100  # width of the rectangle
height = 100  # height of the rectangle

# make a pygame.Rect rectangle
# the syntax is `myvar = pygame.Rect(top-left x, top-left y, width, height)`
# with 0 as top-left x value, 100 as top-left y value,
# width = 50, height = 100
green_rectangle = pygame.Rect(0, 100, 50, 100)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # move a rectangle that isn't a pygame.Rect object
    x += 5  # move to the right 1 px
    y += 5  # move down 1 px

    # erase the previous frame
    window.fill((0, 0, 0))

    # draw a rectangle that isn't a pygame.Rect object
    if x < 400:
        pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    else:
        x, y = 0, 0

    # update the screen
    pygame.display.update()

    pygame.time.wait(50)  # wait 50 milliseconds between frame

pygame.quit()
