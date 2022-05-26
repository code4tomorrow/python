#Create a program that increments a counter every time the space bar is pressed. 
#This counter should be displayed as text on the pygame window.

import pygame
 
pygame.init()
screen = pygame.display.set_mode((400, 400))
 
font = pygame.font.SysFont('arial', 70)

display_counter = 0

run = True
 
while run:

	# Render the "display_counter" to the screen 

	show_counter = font.render(str(display_counter), True, (255,192,203))
	
	# Makes Screen Black

	screen.fill((0, 0, 0))

	# Prints Data on Screen

	screen.blit(show_counter, (30,30))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		# Checks to see if key is pressed
		if event.type == pygame.KEYDOWN:

			# Checks to see if the space is pressed
			if event.key == pygame.K_SPACE:

				# Adds one to the counter 
				display_counter += 1 

		# Updates the data
		pygame.display.update()
		
pygame.quit()
