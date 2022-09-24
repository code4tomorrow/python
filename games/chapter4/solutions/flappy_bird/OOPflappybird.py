import pygame
import random

pygame.init()

# screen
width = 800
height = 600
SIZE = (width, height)
screen = pygame.display.set_mode(SIZE)

# colors
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

# images
BACKGROUNDIMG = pygame.image.load("./background.png")
BACKGROUNDIMG = pygame.transform.scale(BACKGROUNDIMG, (width, height))
SPRITESHEET = pygame.image.load("./flyingbird.png")
COINPIC = pygame.image.load("./coin.png")

# ---------- States of the Game ----------
MENUSTATE = 0  # Menu Screen
GAMESTATE = 1  # Play Game
LOSESTATE = 2  # u loose
QUITSTATE = 3
NUMSTATES = 4


class GameObj:
    """
    An abstract class used as the base class for all the
    game's objects
    """

    def __init__(self):
        """
        This __init__ method provides no functionality.
        It merely enables the methods defined in this class.
        Thus, calling super().__init__ is unnecessary.
        """
        self.rect = pygame.Rect

    def draw(
        self,
        screen: pygame.Surface,
        color: tuple,
        specific_rect: pygame.Rect = None,
    ):
        """
        Draws a rectangle onto the screen in the specified color.
        If specific_rect is not None, draw specific_rect onto the screen.
        If specific_rect is None, draw self.rect onto the screen.
        """
        if not specific_rect:
            pygame.draw.rect(screen, color, self.rect)
        else:
            pygame.draw.rect(screen, color, specific_rect)

    def move(self, speed: dict = None, specific_rect: pygame.Rect = None):
        """
        Moves a rectangle.
        @param speed - The speed to move the rectangle at. It should be
        a dictionary of form {'x': int, 'y': int}; for example,
        {'x':33, 'y':-22}. If no speed is provided, uses self.speed
        @param specific_rect - if specific_rect is None, then this method
        will move self.rect. If specific_rect is not None, then this method will
        move specific_rect
        """
        if not speed and hasattr(self, "speed"):
            if specific_rect:
                return specific_rect.move(self.speed["x"], self.speed["y"])
            else:
                self.rect = self.rect.move(self.speed["x"], self.speed["y"])
        if speed:
            if specific_rect:
                return specific_rect.move(speed["x"], speed["y"])
            else:
                self.rect = self.rect.move(speed["x"], speed["y"])

    def check_collision(self, other, specific_rect: pygame.Rect = None):
        if not specific_rect:
            return self.rect.colliderect(other.rect) == 1
        else:
            return specific_rect.colliderect(other.rect) == 1


class Tubes(GameObj):
    """
    Class to represent the two tubes.

    Ex:
    The tubes will look sort of like the below drawing
    (one on the top, one on the bottom)
    (let - be top or bottom of school)
    ------------
        | |
        |_|

         _
        | |
        | |
        | |
    ------------
    """

    TUBEGAP = 230  # smaller TUBEGAP -> smaller dist between tubes
    TUBEWIDTH = 100

    def __init__(self, bottom_tube_height: int):
        """
        Initializes two pygame.Rect objects: one for the
        top tube (call it top_tube) and one for the bottom tube
        (call it bottom_tube). Uses the TUBEGAP
        and TUBEWIDTH variables as dimensions.
        """
        self.bottom_tube = pygame.Rect(
            width,
            height - bottom_tube_height,
            self.TUBEWIDTH,
            bottom_tube_height,
        )
        self.top_tube = pygame.Rect(
            width,
            0,
            self.TUBEWIDTH,
            height - bottom_tube_height - self.TUBEGAP,
        )

    def draw(self, screen: pygame.Surface):
        """
        Uses the draw() method from the inherited
        GameObj class to draw the top and bottom tubes.
        Hint: this will use the specific_rect argument
        """
        super().draw(screen, DGREEN, self.bottom_tube)
        super().draw(screen, DGREEN, self.top_tube)

    def move(self, speed: dict):
        """
        Uses the move() method from the inherited
        GameObj class to move the specific top and bottom tubes.
        Hint: this will use the specific_rect argument
        """
        self.bottom_tube = super().move(speed, self.bottom_tube)
        self.top_tube = super().move(speed, self.top_tube)

    def check_collision(self, other) -> bool:
        """
        Uses the check_collision() method from the inherited
        GameObj class to check for any collisions
        between the given object and the tubes.
        Hint: this will use the specific_rect argument

        Returns:
            boolean - if either tube is collided with, return True
        """
        bottom = super().check_collision(other, self.bottom_tube)
        top = super().check_collision(other, self.top_tube)
        return bottom or top


class Coin(GameObj):
    """
    The coin that the bird will get
    in-between tubes.
    Doesn't need to do anything, so pretty short class.
    """

    def __init__(self, center_y):
        """
        Makes a coin object.
        The coin's x coordinate will be the width of the screen
        The coin's y coordinate will be centered around `center_y`
        @param center_y:int - the y coordinate to center the coin around
        """
        temprect = COINPIC.get_rect()
        self.rect = pygame.Rect(
            width,
            center_y - temprect.height // 2,
            temprect.width,
            temprect.height,
        )

    def draw(self, screen: pygame.Surface):
        super().draw(screen, BLACK)

    def blit(self, screen: pygame.Surface):
        screen.blit(COINPIC, self.rect)


class Bird(GameObj):
    """
    The bird itself. It processes the sprites
    and handles jumping.
    """

    start_center_pos = (width // 8, height // 2)

    def __init__(self):
        self.process_spritesheet(SPRITESHEET, 3, 3)
        self.rect = pygame.Rect(
            self.start_center_pos[0] - self.sprite_frame_width // 2,
            self.start_center_pos[1] - self.sprite_frame_height // 2,
            self.sprite_frame_width,
            self.sprite_frame_height,
        )
        self.momentum = 0  # the bird's current vertical speed
        self.jump_height = 15
        self.min_speed = -10  # the maximum speed the bird flies down at
        self.cur_sprite_idx = 0

    def process_spritesheet(
        self,
        spritesheet: pygame.Surface,
        num_pics_x: int,
        num_pics_y: int,
        offset_x: int = 0,
        offset_y: int = 0,
    ):
        """
        Creates sprites from the spritesheet.
        @param spritesheet: pygame.Surface - the spritesheet.
        @param num_pics_x: int - the number of sprites in each row on
        the spritesheet
        @param num_pics_y: int - the number of sprites in each column
        on the spritesheet
        @param offset_x: int - the x offset before the sprite rows start
        @param offset_y: int - the y offset before the sprite columns start
        """
        self.sprites = []
        self.sprite_frame_width = (
            spritesheet.get_width() - offset_x
        ) // num_pics_x
        self.sprite_frame_height = (
            spritesheet.get_height() - offset_y
        ) // num_pics_y
        for row in range(num_pics_x):
            for column in range(num_pics_y):
                temp = spritesheet.subsurface(
                    (
                        row * self.sprite_frame_width + offset_x,
                        column * self.sprite_frame_height + offset_y,
                        self.sprite_frame_width,
                        self.sprite_frame_height,
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
        if curr_sprite_idx != self.cur_sprite_idx:
            # if it is now a different sprite, adjust self.rect
            # so that it won't be bigger or smaller than the new sprite
            self.cur_sprite_idx = curr_sprite_idx
            temp = self.sprites[self.cur_sprite_idx]
            self.rect = temp.get_rect().move(
                self.rect.topleft[0], self.rect.topleft[1]
            )
        super().draw(screen, BLACK)

    def blit(self, screen: pygame.Surface):
        screen.blit(self.sprites[self.cur_sprite_idx], self.rect)

    def process_movement(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            self.momentum = self.jump_height

    def move(self):
        super().move({"x": 0, "y": -self.momentum})
        self.momentum -= 1

        # if the bird would fly down faster than self.min_speed,
        # cap self.momentum at self.min_speed
        if self.momentum < self.min_speed:
            self.momentum = self.min_speed


class Button(GameObj):
    """
    A Button with text. Used for the
    'Quit Game' 'Start Game' and 'Retry' buttons
    """

    def __init__(
        self,
        center_x: int,
        center_y: int,
        bgcolor: tuple,
        textcolor: tuple,
        text: str = "",
        textsize: int = 32,
    ):
        """
        Creates a Button object.
        @param center_x: int - the x coordinate of the button's center
        @param center_y: int - the y coordinate of the button's center
        @param bgcolor: tuple - the color for the button's background
        @param textcolor: tuple - the color for the button's text
        @param text: str - the text to put inside the button
        @param textsize: int - the size of the button's text
        """
        self.font = pygame.font.SysFont("arial", textsize)
        self.font_img = self.font.render(text, True, textcolor)
        self.rect = self.font_img.get_rect()
        self.rect.center = (center_x, center_y)
        self.bgcolor = bgcolor
        self.active = True

    def draw(self, screen: pygame.Surface):
        super().draw(screen, self.bgcolor)
        screen.blit(self.font_img, self.rect)

    def is_clicked(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return event.pos in self

    def __contains__(self, coordinate):
        return self.rect.contains((coordinate[0], coordinate[1], 0, 0))


class FlappyBird:
    """
    This is the game class.
    """

    def __init__(self):
        self.running = True
        self.gamestate = MENUSTATE
        self.create_buttons()
        self.framecount = 0
        self.clock = pygame.time.Clock()

    def create_buttons(self, button1text="Start Game", button2bg=RED):
        self.buttons = {
            "start": Button(
                width // 2, height // 4, LGREEN, LILAC, button1text
            ),
            "quit": Button(
                width // 2, height // 4 * 3, button2bg, LILAC, "Quit Game"
            ),
        }

    def mainloop(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                self.set_state(event)
                if event.type == pygame.QUIT:
                    self.running = False
            if self.gamestate == MENUSTATE:
                screen.fill(LBLUE)
                self.draw_buttons(screen)

            elif self.gamestate == GAMESTATE:
                self.draw_all()
                self.check_collisions()

                # update bird's speed
                for event in events:
                    self.bird.process_movement(event)
                self.moveobjects()

                self.create_tubes()

            elif self.gamestate == LOSESTATE:
                screen.fill(RED)
                self.draw_buttons(screen)

            elif self.gamestate == QUITSTATE:
                self.running = False

            self.framecount += 1
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()

    def set_state(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if all([but.active for but in self.buttons.values()]):
                if self.buttons["start"].is_clicked(event):
                    self.buttons["start"].active = False
                    self.buttons["quit"].active = False
                    self.startgame()
                elif self.buttons["quit"].is_clicked(event):
                    self.gamestate = QUITSTATE
                    self.buttons["start"].active = False
                    self.buttons["quit"].active = False

    def draw_background(self):
        screen.blit(BACKGROUNDIMG, (self.background_x, 0))
        screen.blit(BACKGROUNDIMG, (self.background_x + width, 0))
        self.background_x -= 2
        if self.background_x < -1 * width:
            self.background_x = 0

    def draw_score(self):
        """
        Writes the player's score onto the screen in the top
        right corner.
        Hint: this uses pygame fonts
        """
        font = pygame.font.SysFont("arial", 32)
        font_img = font.render(f"Score : {self.score}", True, WHITE)
        screen.blit(font_img, font_img.get_rect().move(width - 200, 0))

    def draw_buttons(self, screen):
        """
        Draws the "start" and "quit" buttons onto the screen.
        Hint: this uses `self.buttons` (which is already made)
        """
        self.buttons["start"].draw(screen)
        self.buttons["quit"].draw(screen)

    def create_tubes(self):
        """
        Creates tubes and puts a coin in the middle of each tube.
        """
        if (
            len(self.tubes) == 0
            or self.tubes[-1].bottom_tube.right < width - 200
        ):
            bottom_tube_height = random.randint(0, height - Tubes.TUBEGAP)
            self.tubes.append(Tubes(bottom_tube_height))
            self.coins.append(
                Coin(height - bottom_tube_height - (Tubes.TUBEGAP // 2))
            )

    def draw_all(self):
        # draw bird and coin rectangles before background so that they won't
        # show
        self.bird.draw(screen, self.framecount)
        for coin in self.coins:
            coin.draw(screen)

        self.draw_background()

        for tube in self.tubes:
            tube.draw(screen)

        # blit images/sprites onto the screen
        self.bird.blit(screen)
        for coin in self.coins:
            coin.blit(screen)

        self.draw_score()

    def check_collisions(self):
        for tube in self.tubes:
            if tube.check_collision(self.bird):
                self.gamestate = LOSESTATE
                self.create_buttons("Retry?", LBLUE)
            if tube.bottom_tube.right < 0:
                self.tubes.remove(tube)

        for coin in self.coins:
            if self.bird.check_collision(coin):
                self.score += 1
                self.coins.remove(coin)
            if coin.rect.right < 0:
                self.coins.remove(coin)

        if self.bird.rect.bottom > height:  # fell out of screen
            self.gamestate = LOSESTATE
            self.create_buttons("Retry?", LBLUE)

    def moveobjects(self):
        SPEED = 3  # x speed that objects move towards the bird at
        for tube in self.tubes:
            tube.move({"x": -SPEED, "y": 0})
        for coin in self.coins:
            coin.move({"x": -SPEED, "y": 0})
        self.bird.move()

    def startgame(self):
        self.gamestate = GAMESTATE
        self.background_x = 0
        self.score = 0
        self.bird = Bird()
        self.tubes = []
        self.coins = []
        self.create_tubes()


a = FlappyBird()
a.mainloop()
