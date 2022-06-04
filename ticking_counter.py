import pygame
import time  # use this to show text

pygame.init()
screen = pygame.display.set_mode((400, 400))  # set frame

fonts = pygame.font.SysFont("arial", 20)  # size of message
font = pygame.font.SysFont("arial", 70)  # size of counter
text = "DON'T PRESS A KEY"  # text
counter = 10  # sets the counter

run = True

while run:
    if pygame.event.peek(pygame.KEYDOWN):  # checks queue for keydown
        counter -= 1  # decreases counter by one
        pygame.event.clear(pygame.KEYDOWN)  # clears keydown from queue
    if counter == 1:  # changes text
        text = "PLEASE YOU'll BLOW US UP!"
    if counter == 0:  # changes text and ends program
        text = "YOU BLEW US UP D:"
        run = False
    # the if statements are before because when
    # run is false, they will still run
    # one last time, showing the last message
    show_message = fonts.render(
        text, True, (255, 102, 253)
    )  # sets the message
    show_counter = font.render(
        str(counter), True, (255, 230, 102)
    )  # sets the counter
    screen.fill((0, 0, 0))  # refreshes every frame
    screen.blit(show_counter, (200, 200))  # shows counter
    screen.blit(show_message, (50, 100))  # shows message
    pygame.display.update()  # updates the frame

time.sleep(1)  # makes the last balue of text readable
pygame.quit()
