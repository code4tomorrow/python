import pygame
import random

# from replit import audio

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

LGREEN = (62, 245, 59)
DGREEN = (40, 143, 39)
YELLOW = (250, 250, 37)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LILAC = (175, 95, 237)
LBLUE = (80, 221, 242)
DBLUE = (80, 99, 242)
PINK = (245, 144, 188)
CYAN = (0, 150, 150)

MENUSTATE = 0
GAMESTATE = 1
LOSESTATE = 2
QUITSTATE = 3
NUMSTATES = 4

KEY_RIGHT = False
KEY_LEFT = False
KEY_UP = False
KEY_DOWN = False
HIT_COIN = False

# img = pygame.image.load('bird.png')
# img.convert()
backgroundimg = pygame.image.load("background.png")
backgroundimg = pygame.transform.scale(backgroundimg, (WIDTH, HEIGHT))
spritesheet = pygame.image.load("flyingbird.png")
coinpic = pygame.image.load("coin.png")


def displaytext(words, color, x, y, size):
    """Draws text on screen"""
    font = pygame.font.SysFont("arial", size)
    text = font.render(words, True, color)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def main_page(screen):
    """Draws menu page"""
    pygame.draw.rect(screen, LBLUE, (0, 0, 800, 600))
    pygame.draw.rect(screen, LGREEN, (150, 100, 500, 100))
    displaytext("Play Flappy Bird", LILAC, 400, 150, 40)
    pygame.draw.rect(screen, LGREEN, (150, 300, 500, 100))
    displaytext("Quit Game :(", LILAC, 400, 350, 40)


def pillars(topGap):
    """Creates pillars"""
    global rectList

    topRect = pygame.Rect(550, 0, 100, topGap)
    bottomRect = pygame.Rect(550, topGap + 230, 100, HEIGHT)
    rectList.append(topRect)
    rectList.append(bottomRect)

    return rectList


def load_sprites(spritesheet, DIMw, DIMh, offset):
    """Loads sprites from spritesheet"""
    sprites = []
    W = spritesheet.get_width() // DIMw  # frame width
    H = spritesheet.get_height() // DIMh  # frame height

    for i in range(DIMw * DIMh - offset):  # offset is if there are extra blank frames
        x = i % DIMw * W  # x coordinate of frame
        y = i // DIMw * H  # y coordinate of frame
        sprites.append(spritesheet.subsurface(pygame.Rect(x, y, W, H)))
        # cuts out the frame onto a subsurface then added to list

    return sprites  # sends the list back to the main program


def movement(birdrect):
    """Controls bird movement"""
    global acceleration, HIT_COIN, score

    if KEY_UP is True and birdrect[1] > 10:
        a = birdrect[1]
        birdrect[1] -= acceleration
        acceleration -= 1
        if birdrect[1] >= a:
            birdrect[1] = a
        if HIT_COIN is True:
            HIT_COIN = False
            score += 1
    else:
        if birdrect[1] < 580:
            birdrect[1] += 4
            if HIT_COIN is True:
                HIT_COIN = False
                score += 1

    return birdrect[1]


def drawCoin(topGap):
    """Draws coins"""
    global rectList

    for element in rectList:
        coinrect = pygame.Rect(element[0], topGap + 100, 70, 70)
        return coinrect


def draw_background(screen, birdrect, backgroundX):
    """Draws background image"""
    global rectList, topGap, score

    screen.blit(backgroundimg, (backgroundX, 0))
    screen.blit(backgroundimg, (backgroundX + WIDTH, 0))
    displaytext("SCORE: " + str(score), WHITE, 600, 30, 32)

    for element in rectList:
        pygame.draw.rect(screen, LGREEN, element)

    # birdrect.center = 300,ypos
    pygame.draw.rect(screen, BLACK, drawCoin(topGap))
    screen.blit(coinpic, drawCoin(topGap))
    pygame.draw.rect(screen, BLACK, birdrect)
    screen.blit(sprites[framecount // 5 % len(sprites)], (birdrect))
    # screen.blit(img, birdrect)


def losepage(screen):
    """Draws loser page"""
    pygame.draw.rect(screen, PINK, (0, 0, screen.get_width(), screen.get_height()))
    pygame.draw.rect(screen, LBLUE, (150, 100, 500, 100))
    displaytext("Play Again?", DBLUE, 400, 150, 40)
    displaytext("YOU LOSE ^-^ ", RED, 400, 250, 70)
    pygame.draw.rect(screen, LGREEN, (150, 300, 500, 100))
    displaytext("Quit Game :(", LILAC, 400, 350, 40)


def getNewState(but, curState, x, y):
    """Updates game state"""
    if but == 1 and curState == MENUSTATE and 150 < x < 650 and 100 < y < 200:
        return GAMESTATE  # during menu state if button clicked, gamestate begins
    elif but == 1 and curState == MENUSTATE and 150 < x < 650 and 300 < y < 400:
        return QUITSTATE
    elif but == 1 and curState == LOSESTATE and 150 < x < 650 and 100 < y < 200:
        print("you lost")
        return GAMESTATE
    elif but == 1 and curState == LOSESTATE and 150 < x < 650 and 300 < y < 400:
        return QUITSTATE
    else:
        print("check test")


def collision(ypos, pilla):
    """Checks for collisions"""
    if ypos.colliderect(pilla):
        return True
    return False


# --------------------------------------MAIN LOOP TIME
myClock = pygame.time.Clock()
running = True

birdrect = pygame.Rect(100, 310, 50, 50)
backgroundX = 0
state = MENUSTATE
rectList = []
rectList = pillars(300)
framecount = 0
topGap = 300
score = 0

while running:
    framecount += 1
    sprites = load_sprites(spritesheet, 3, 3, 0)

    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False

        # checks keyboard events
        if evnt.type == pygame.KEYDOWN:
            if evnt.key == pygame.K_LEFT:
                KEY_LEFT = True
            if evnt.key == pygame.K_RIGHT:
                KEY_RIGHT = True
            if evnt.key == pygame.K_UP and KEY_UP is False:
                KEY_UP = True
                acceleration = 15
        if evnt.type == pygame.KEYUP:
            if evnt.key == pygame.K_LEFT:
                KEY_LEFT = False
            if evnt.key == pygame.K_RIGHT:
                KEY_RIGHT = False
            if evnt.key == pygame.K_UP:
                KEY_UP = False

        # checks mouse events
        if evnt.type == pygame.MOUSEBUTTONDOWN:
            button = evnt.button
            a, b = evnt.pos
            state = getNewState(button, state, a, b)

    # -----------------------------------------EXIT FOR LOOP
    # CHECK FOR STATE AND EXCECUTE BASED ON SPECIFIC STATE
    if state == MENUSTATE:
        main_page(screen)
    if state == GAMESTATE:
        birdrect[1] = movement(birdrect)
        draw_background(screen, birdrect, backgroundX)
        backgroundX -= 2
        if backgroundX < -1 * WIDTH:
            backgroundX = 0
        for element in rectList:
            element[0] -= 3
            if element[0] < 70:
                rectList.clear()
                topGap = random.randint(150, 450)
                rectList = pillars(topGap)
                drawCoin(topGap)
        for element in rectList:
            if collision(birdrect, element) is True:
                state = LOSESTATE
        if collision(birdrect, drawCoin(topGap)) is True and drawCoin(topGap)[0] == 145:
            HIT_COIN = True
            # print(score)
            # fix collision and check jump
    if state == LOSESTATE:
        losepage(screen)
        birdrect = pygame.Rect(100, 310, 50, 50)
        backgroundX = 0
        rectList = []
        rectList = pillars(300)
        framecount = 0
        topGap = 300  # initial value
        score = 0
    if state == QUITSTATE:
        running = False

    pygame.display.flip()
    myClock.tick(60)

pygame.quit()
