import pygame

pygame.init()

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Drawing and Moving Objects")

BLACK = (0, 0, 0)  # background color
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# make a rectangle without the pygame.Rect class
x = 100  # top-left x value
y = 400  # top-left y value
width = 100  # width of the rectangle
height = 50  # height of the rectangle

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
    x += 1  # move to the right 1 px
    y += 1  # move down 1 px

    # move a rectangle that is a pygame.Rect object
    green_rectangle.move_ip(1, 2)  # moves 1 to the right, 2 down
    # this is equivalent to green_rectangle = green_rectangle.move(1, 2)

    # erase the previous frame
    window.fill(BLACK)

    # draw a rectangle that isn't a pygame.Rect object
    pygame.draw.rect(window, RED, (x, y, width, height))

    # draw a rectangle that is a pygame.Rect object
    pygame.draw.rect(window, GREEN, green_rectangle)

    # update the screen
    pygame.display.update()

    # sometimes you need to limit frame rate or your objects
    # will seem to move too fast
    pygame.time.wait(30)  # wait 30 milliseconds between frame

pygame.quit()  # close pygame after finishing
