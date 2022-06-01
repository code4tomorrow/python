import pygame

pygame.init()

window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Drawing and Moving Objects")


# make a rectangle without the pygame.Rect class
x = 0  # top-left x value
y = 0  # top-left y value
width = 100  # width of the rectangle
height = 100  # height of the rectangle
