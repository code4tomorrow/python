import pygame
pygame.init()
 
flag = pygame.locals.RESIZABLE
window = pygame.display.set_mode((500, 400), flag)
 
pygame.event.set_blocked(pygame.KEYDOWN)
 
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # if event is QUIT
			run = False
        if event.type == pygame.KEYUP:
            # if event is KEYUP
            print(“Up up up!”)
        if event.type == pygame.KEYDOWN:
            # this will never happen because KEYDOWN is blocked
            print(“Down down down!”)
 
pygame.quit()
