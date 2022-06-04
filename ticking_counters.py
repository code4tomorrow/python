# make a time bomb!

# Create a counter that starts at a number, such
# 10 and goes down everytime the user presses
# the keyboard. However, this is a time bomb!
# create some text to warn the user, and when the
# number gets low, switch the message. Then, when
# the number hits zero, switch the message again
# to show that they've blown up, and exit the program.
# Make sure to use some of the methods featured in 3.4!

# imports!

screen = pygame.display.set_mode((400, 400))

# feel free to change these values
fonts = pygame.font.SysFont("arial", 20)
font = pygame.font.SysFont("arial", 70)
text = "DON'T PRESS A KEY"
counter = 10
