# TODO : modify bird's rect every time the sprite is changed since
# now only the sprite is seen, so it might confuse the user if the
# sprite is visibly not touching a tube but they lost because the
# rectangle the sprite is blit'ed on touched the tube.

import pygame
import random

pygame.init()
SIZE = (800, 600)
screen = pygame.display.set_mode(SIZE)
width = 800
height = 600
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

myClock = pygame.time.Clock()
BACKGROUNDIMG = pygame.image.load(
    "C:/Projects/python_repo/games/chapter4/solutions/flappy_bird/background.png"
)
BACKGROUNDIMG = pygame.transform.scale(BACKGROUNDIMG, (width, height))
SPRITESHEET = pygame.image.load(
    "C:/Projects/python_repo/games/chapter4/solutions/flappy_bird/flyingbird.png"
)

COINPIC = pygame.image.load(
    "C:/Projects/python_repo/games/chapter4/solutions/flappy_bird/coin.png"
)
# ---------- States of the Game ----------
MENUSTATE = 0  # Menu Screen
GAMESTATE = 1  # Play Game
LOSESTATE = 2  # u loose
QUITSTATE = 3
NUMSTATES = 4


class GameObj:
    def __init__(self):
        """
        This __init__ method provides no functionality.
        It merely enables the methods defined in this class.
        Thus, calling super().__init__ is unnecessary.
        """
        self.rect = pygame.Rect

    def draw(self, screen, color, specificRect: pygame.Rect = None):
        if not specificRect:
            pygame.draw.rect(screen, color, self.rect)
        else:
            pygame.draw.rect(screen, color, specificRect)

    def move(self, speed: dict = None, specificRect: pygame.Rect = None):
        if not speed and hasattr(self, "speed"):
            if specificRect:
                return specificRect.move(self.speed["x"], self.speed["y"])
            else:
                self.rect = self.rect.move(self.speed["x"], self.speed["y"])
        if speed:
            if specificRect:
                return specificRect.move(speed["x"], speed["y"])
            else:
                self.rect = self.rect.move(speed["x"], speed["y"])

    def checkcollision(self, other, specifiedRect=None):
        if not specifiedRect:
            return self.rect.colliderect(other.rect) == 1
        else:
            return specifiedRect.colliderect(other.rect) == 1


class Tubes(GameObj):
    TUBEGAP = 230  # smaller TUBEGAP -> smaller dist between tubes
    TUBEWIDTH = 100

    def __init__(self, bottomTubeHeight):
        self.bottomRect = pygame.Rect(
            width, height - bottomTubeHeight, self.TUBEWIDTH, bottomTubeHeight
        )
        self.topRect = pygame.Rect(
            width, 0, self.TUBEWIDTH, height - bottomTubeHeight - self.TUBEGAP
        )

    def draw(self, screen):
        super().draw(screen, DGREEN, self.bottomRect)
        super().draw(screen, DGREEN, self.topRect)

    def move(self, speed):
        self.bottomRect = super().move(speed, self.bottomRect)
        self.topRect = super().move(speed, self.topRect)

    def checkcollision(self, other):
        bottom = super().checkcollision(other, self.bottomRect)
        top = super().checkcollision(other, self.topRect)
        return bottom or top


class Coin(GameObj):
    def __init__(self, yCenter):
        temprect = COINPIC.get_rect()
        self.rect = pygame.Rect(
            width,
            yCenter - temprect.height // 2,
            temprect.width,
            temprect.height,
        )

    def draw(self, screen):
        super().draw(screen, BLACK)

    def blit(self, screen):
        screen.blit(COINPIC, self.rect)


class Bird(GameObj):
    startCenterPos = (width // 8, height // 2)

    def __init__(self):
        self.processSpritesheet(SPRITESHEET, 3, 3)
        self.rect = pygame.Rect(
            self.startCenterPos[0] - self.spriteFrameWidth // 2,
            self.startCenterPos[1] - self.spriteFrameHeight // 2,
            self.spriteFrameWidth,
            self.spriteFrameHeight,
        )
        self.upmomentum = 0
        self.goingup = False
        self.curSpriteIdx = 0

    def processSpritesheet(
        self,
        Spritesheet: pygame.Surface,
        numPicsX: int,
        numPicsY: int,
        xOffset: int = 0,
        yOffset: int = 0,
    ):
        self.sprites = []
        self.spriteFrameWidth = (Spritesheet.get_width() - xOffset) // numPicsX
        self.spriteFrameHeight = (
            Spritesheet.get_height() - yOffset
        ) // numPicsY
        for row in range(numPicsX):
            for column in range(numPicsY):
                temp = Spritesheet.subsurface(
                    (
                        row * self.spriteFrameWidth + xOffset,
                        column * self.spriteFrameHeight + yOffset,
                        self.spriteFrameWidth,
                        self.spriteFrameHeight,
                    )
                )
                # get the bounding box for the actual colored pixels
                # (so that we won't be blit-ing extra empty pixels)
                # (makes collisions more accurate)
                temprect = temp.get_bounding_rect()
                # then, append the shortened image to the sprites list
                self.sprites.append(temp.subsurface(temprect))

    def draw(self, screen: pygame.Surface, framecount: int):
        curr_sprite_idx = framecount // 5 % len(self.sprites)
        if curr_sprite_idx != self.curSpriteIdx:
            # if it is now a different sprite, adjust self.rect
            # so that it won't be bigger or smaller than the new sprite
            self.curSpriteIdx = curr_sprite_idx
            temp = self.sprites[self.curSpriteIdx]
            self.rect = temp.get_rect().move(
                self.rect.topleft[0], self.rect.topleft[1]
            )
        super().draw(screen, BLACK)

    def blit(self, screen: pygame.Surface):
        screen.blit(self.sprites[self.curSpriteIdx], self.rect)

    def movement(self, event):
        JUMPHEIGHT = 15
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.goingup = True
            self.upmomentum = JUMPHEIGHT

        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            self.goingup = False

    def move(self):
        if self.goingup and self.upmomentum >= 0:
            if self.rect[1] > 0:
                super().move({"x": 0, "y": -self.upmomentum})
            self.upmomentum -= 1
        else:
            super().move({"x": 0, "y": 4})


class button(GameObj):
    def __init__(
        self,
        centerx,
        centery,
        bgcolor: tuple,
        textcolor: tuple,
        text="",
        textsize=32,
    ):
        self.font = pygame.font.SysFont("arial", textsize)
        self.fontimg = self.font.render(text, True, textcolor)
        self.rect = self.fontimg.get_rect()
        self.rect.center = (centerx, centery)
        self.bgcolor = bgcolor
        self.active = True

    def draw(self, screen: pygame.Surface):
        super().draw(screen, self.bgcolor)
        screen.blit(self.fontimg, self.rect)

    def isclicked(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return event.pos in self

    def __contains__(self, coordinate):
        return self.rect.contains((coordinate[0], coordinate[1], 0, 0))


class flappybird:
    def __init__(self):
        self.running = True
        self.gamestate = MENUSTATE
        self.createButtons()
        self.framecount = 0
        self.clock = pygame.time.Clock()

    def createButtons(self, button1text="Start Game", button2bg=RED):
        self.buttons = {
            "start": button(
                width // 2, height // 4, LGREEN, LILAC, button1text
            ),
            "quit": button(
                width // 2, height // 4 * 3, button2bg, LILAC, "Quit Game"
            ),
        }

    def mainloop(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                self.setstate(event)
                if event.type == pygame.QUIT:
                    self.running = False
            if self.gamestate == MENUSTATE:
                screen.fill(LBLUE)
                self.drawbuttons(screen)

            elif self.gamestate == GAMESTATE:
                self.drawAll()
                self.checkcollisions()

                # update bird's speed
                for event in events:
                    self.bird.movement(event)
                self.moveobjects()

                self.create_tubes()

            elif self.gamestate == LOSESTATE:
                screen.fill(RED)
                self.drawbuttons(screen)

            elif self.gamestate == QUITSTATE:
                self.running = False

            self.framecount += 1
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()

    def setstate(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if all([but.active for but in self.buttons.values()]):
                if self.buttons["start"].isclicked(event):
                    self.buttons["start"].active = False
                    self.buttons["quit"].active = False
                    self.startgame()
                elif self.buttons["quit"].isclicked(event):
                    self.gamestate = QUITSTATE
                    self.buttons["start"].active = False
                    self.buttons["quit"].active = False

    def drawbackground(self):
        screen.blit(BACKGROUNDIMG, (self.backgroundX, 0))
        screen.blit(BACKGROUNDIMG, (self.backgroundX + width, 0))
        self.backgroundX -= 2
        if self.backgroundX < -1 * width:
            self.backgroundX = 0

    def drawscore(self):
        font = pygame.font.SysFont("arial", 32)
        fontimg = font.render(f"Score : {self.score}", True, WHITE)
        screen.blit(fontimg, fontimg.get_rect().move(width - 200, 0))

    def drawbuttons(self, screen):
        self.buttons["start"].draw(screen)
        self.buttons["quit"].draw(screen)

    def create_tubes(self):
        if (
            len(self.tubes) == 0
            or self.tubes[-1].bottomRect.right < width - 200
        ):
            bottomtubeheight = random.randint(0, height - Tubes.TUBEGAP)
            self.tubes.append(Tubes(bottomtubeheight))
            self.coins.append(
                Coin(height - bottomtubeheight - (Tubes.TUBEGAP // 2))
            )

    def drawAll(self):
        # draw bird and coin rectangles before background so that they won't
        # show
        self.bird.draw(screen, self.framecount)
        for coin in self.coins:
            coin.draw(screen)

        self.drawbackground()

        for tube in self.tubes:
            tube.draw(screen)

        # blit images/sprites onto the screen
        self.bird.blit(screen)
        for coin in self.coins:
            coin.blit(screen)

        self.drawscore()

    def checkcollisions(self):
        for tube in self.tubes:
            if tube.checkcollision(self.bird):
                self.gamestate = LOSESTATE
                self.createButtons("Retry?", LBLUE)
            if tube.bottomRect.right < 0:
                self.tubes.remove(tube)

        for coin in self.coins:
            if self.bird.checkcollision(coin):
                self.score += 1
                self.coins.remove(coin)
            if coin.rect.right < 0:
                self.coins.remove(coin)

        if self.bird.rect.bottom > height:  # fell out of screen
            self.gamestate = LOSESTATE
            self.createButtons("Retry?", LBLUE)

    def moveobjects(self):
        SPEED = 3
        for tube in self.tubes:
            tube.move({"x": -SPEED, "y": 0})
        for coin in self.coins:
            coin.move({"x": -SPEED, "y": 0})
        self.bird.move()

    def startgame(self):
        self.gamestate = GAMESTATE
        self.backgroundX = 0
        self.score = 0
        self.bird = Bird()
        self.tubes = []
        self.coins = []
        self.create_tubes()


a = flappybird()
a.mainloop()
