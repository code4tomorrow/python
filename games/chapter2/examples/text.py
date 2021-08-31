import pygame
from pygame.locals import RESIZABLE

pygame.init()
flag = RESIZABLE
window = pygame.display.set_mode((500, 400), flag)
pygame.display.set_caption("Text!")
WHITE = (255, 255, 255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # step 1 to writing: load the font with pygame.font.SysFont(font, size)
    # For font - You can either use the default font
    # (pygame.font.get_default_font()) or use a font name
    # (like Comic Sans or Arial).
    # For size - a positive integer representing the font size.
    font = pygame.font.SysFont("Arial", 32)

    # step 2 - render the font with
    # (font variable name).render(
    #   text: string, antialias: bool, color: tuple, background=None
    # )
    # In this case, we render the text "Hello World!", pass True as antiaalias
    # and have the color of the text be WHITE
    text = font.render("Hello World!", True, WHITE)

    # step 3 - blit to the screen
    # You can either blit the text to a rectangle on the screen or a specified
    # coordinate
    # In this case, we blit (draw) the text with a top-left value of (0, 0)
    window.blit(text, (100, 100))

    # update the screen; just like with moving/displaying rectangles
    pygame.display.update()

pygame.quit()
