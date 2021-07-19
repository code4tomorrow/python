import pygame
from pygame import Surface
import uuid

from pygame.locals import *
import time
import math
import random

BULLET_IMG_PATH = "./bullet.png"
TARGET_IMG_PATH = "./target.png"
TANK_IMG_PATH = "./completetank.png"

BLACK = (255, 255, 255)
DIRTBROWN = (168, 95, 0)
SANDBROWN = (237, 201, 175)

TANKSPEED = [2, 2]  # speed x and speed y
BULLETSPEED = [8, 8]


class Game_obj:
    def __init__(self, picture: str, **kwargs) -> None:
        """
        A basic game object class. It handles collisions
        and has a uuid (universally unique identifier)

        Arguments:
            picture:str - the location of the picture that will be displayed on
                the screen for this object
            Valid keyword arguments:
                "size":tuple(x,y) - a specific size that you want to have the object be.
                    The picture will be scaled to that size and the hitbox
                    will be updated accordingly.
                "position":tuple(x,y) - the tuple at which the top left of the object
                    should be positioned at
                "speed":tuple(x,y) - the tuple that represents the object's speed.
        """
        self.uuid = uuid.uuid4()
        self.name = ""

        # self.image will be a pygame.image.Surface class
        self.image = pygame.image.load(picture)
        self.image = (
            pygame.transform.scale(
                self.image, (kwargs["size"][0], kwargs["size"][1])
            )
            if "size" in kwargs
            else self.image
        )

        self.rect = (
            self.image.get_rect()
        )  # self.rect will be of pygame.Rect class
        self.size = self.rect.size  # will be a tuple of (sizex, sizey)

        if "position" in kwargs:
            self.moveto(kwargs["position"])

        self.speed = (
            {"x": kwargs["speed"][0], "y": kwargs["speed"][1]}
            if "speed" in kwargs
            else {"x": 0, "y": 0}
        )

    def check_collision(self, other: object) -> bool:
        if not isinstance(other, Game_obj):
            raise TypeError(
                "Invalid type; need a game_obj or a child class of game_obj"
            )
        return self.rect.colliderect(other.rect) == 1  # 1 if True, 0 if False

    def draw(self, screen: Surface, color: tuple) -> None:
        pygame.draw.rect(screen, color, self.rect, 0)
        screen.blit(self.image, self.rect)

    def move(self) -> None:
        """
        Moves the object according to it's current speed.
        """
        self.rect = self.rect.move(self.speed["x"], self.speed["y"])
        # self.draw(screen, color)

    def set_speed(self, new_speed: tuple) -> None:
        """
        Sets the object's speed to the provided tuple
        Arguments:
            new_speed (tuple(x,y)) - a tuple containing the desired speed for
                the object to have.
        """
        self.speed["x"], self.speed["y"] = new_speed[0], new_speed[1]

    def moveto(self, position: tuple) -> None:
        """
        A helper function that moves the rectangle to the desired position.

        Arguments:
            position (tuple) - the x and y coordinates of where you want the rectangle's
                top left to be moved to.
        """
        self.rect = self.rect.move(
            position[0] - self.rect.topleft[0],
            position[1] - self.rect.topleft[1],
        )

    def check_out_of_screen(self, screen_size: tuple) -> bool:
        """
        Checks whether or not the object is completely outside of the screen.
        Returns True or False accordingly.
        Arguments:
            screen_size (tuple) - the size of the screen (x,y)
        """
        if (
            self.rect.bottom > screen_size[1]
            or self.rect.top < 0
            or self.rect.left < 0
            or self.rect.right > screen_size[0]
        ):
            return True
        return False

    def __str__(self):
        return (
            f"{self.name} object located at the position {self.rect.topleft} with"
            + f" uuid {self.uuid}"
        )


class Bullet(Game_obj):
    def __init__(self, **kwargs) -> None:
        super().__init__(BULLET_IMG_PATH, **kwargs)
        self.name = "Bullet"


class Target(Game_obj):
    def __init__(self, **kwargs) -> None:
        kwargs["size"] = 40, 40
        super().__init__(TARGET_IMG_PATH, **kwargs)
        self.name = "Target"


class Tank(Game_obj):
    def __init__(self, **kwargs) -> None:
        super().__init__(TANK_IMG_PATH, **kwargs)
        self.direction = [0, 0]
        self.SPEED = kwargs["speed"] if "speed" in kwargs else [2, 2]
        self.speed["x"], self.speed["y"] = 0, 0

    def set_speed(self) -> None:
        # use math stuff to calculate the speed given that the
        # max speed is self.SPEED
        self.speed["x"] = (
            self.direction[0]
            / math.sqrt(sum(abs(num) for num in self.direction))
            * self.SPEED[0]
            if (sum(abs(num) for num in self.direction)) != 0
            else self.direction[0] * self.SPEED[0]
        )
        self.speed["y"] = (
            self.direction[1]
            / math.sqrt(sum(abs(num) for num in self.direction))
            * self.SPEED[1]
            if (sum(abs(num) for num in self.direction)) != 0
            else self.direction[1] * self.SPEED[1]
        )

    def set_path(self, direction: str) -> None:
        if direction == "up":
            self.direction[1] -= 1
        if direction == "down":
            self.direction[1] += 1
        if direction == "left":
            self.direction[0] -= 1
        if direction == "right":
            self.direction[0] += 1

    def unset_path(self, direction: str) -> None:
        if direction == "up":
            self.direction[1] += 1
        if direction == "down":
            self.direction[1] -= 1
        if direction == "left":
            self.direction[0] += 1
        if direction == "right":
            self.direction[0] -= 1


class App:
    def __init__(
        self, flags=RESIZABLE, width=960, height=540, title="My Game"
    ):
        pygame.init()
        self.size = [width, height]
        self.screen = pygame.display.set_mode(self.size, flags)
        pygame.display.set_caption(title, title)

        self.running = True

        self.create_objects()

    def create_objects(self):
        pass

    def check_events(self, event):
        pass

    def update_display(self):
        pass

    def move_objects(self):
        pass

    def check_collisions(self):
        pass

    def mainloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    break
                else:
                    self.check_events(event)  # this will handle checking for user input
                    # such as KEYUP and MOUSEBUTTONDOWN events needed to run the game
            self.check_collisions()  # checks collisions between bullets (or tanks) and targets
            self.move_objects()  # moves each object on the screen
            self.update_display()  # actually updates the screen (draw each object onto the screen)
            pygame.display.update()  # pygame’s method to show the updated screen
            time.sleep(0.01)  # not necessary; it's a frame cap
        pygame.quit()



class Tank_Game(App):
    def __init__(self):
        super().__init__(title="Tanks")

        self.playerscore = 0  # the player's score

        # this can be changed, it's the number of targets allowed at a time.
        self.NUM_TARGETS = 3

        # sets the display icon to the TankIcon.png provided
        pygame.display.set_icon(pygame.image.load("./TankIcon.png"))

    def create_objects(self):
        """
        This creates the initial objects seen when the game
        first starts up.
        """
        # tank
        self.tank = Tank(speed=TANKSPEED)
        self.tank.moveto(
            (
                self.size[0] / 2 - self.tank.size[0],  # move to middle x
                self.size[1] - self.tank.size[1],  # move to bottom y
            )
        )

        # targets
        self.targets = [Target(speed=[0, 0]) for i in range(self.NUM_TARGETS)]
        for target in self.targets:
            target.moveto(
                (
                    random.randint(0, self.size[0] - target.size[0]),  # random x
                    random.randint(0, self.size[1] - target.size[1]),  # random y
                )
            )

        # bullets
        self.bullets = []

        # Score text
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 32)

    def check_events(self, event):
        """
        We imported all from pygame.locals, so that means
        that we can check KEYDOWN and KEYUP and individual
        keys such as K_w (w key), K_a (a key), etc.
        """
        # change the path of the tank if w, a, s, or d was pressed
        if event.type == KEYDOWN:
            if event.key == K_w:
                self.tank.set_path("up")
            if event.key == K_s:
                self.tank.set_path("down")
            if event.key == K_a:
                self.tank.set_path("left")
            if event.key == K_d:
                self.tank.set_path("right")
        if event.type == KEYUP:
            if event.key == K_w:
                self.tank.unset_path("up")
            if event.key == K_s:
                self.tank.unset_path("down")
            if event.key == K_a:
                self.tank.unset_path("left")
            if event.key == K_d:
                self.tank.unset_path("right")
        self.tank.set_speed()

        # create bullets if mouse button was pressed
        if event.type == MOUSEBUTTONDOWN:
            bul = Bullet(speed=BULLETSPEED)
            bul.moveto(
                (self.tank.rect.centerx, (self.tank.rect.top - bul.size[1]))
            )

            # math stuff to calculate trajectory
            mouse_pos = pygame.mouse.get_pos()
            h = mouse_pos[1] - bul.rect.center[1]
            w = mouse_pos[0] - bul.rect.center[0]
            hyp = math.sqrt(h ** 2 + w ** 2)
            vertical_speed = (
                BULLETSPEED[1] * (h / hyp) if hyp != 0 else BULLETSPEED[1] * h
            )
            horizontal_speed = (
                BULLETSPEED[0] * (w / hyp) if hyp != 0 else BULLETSPEED[0] * w
            )

            bul.set_speed((horizontal_speed, vertical_speed))
            self.bullets.append(bul)

    def move_objects(self):
        """
        This method moves the objects within the game.
        If a bullet is outside of the screen, it is
        not moved and is unreferenced.
        """
        self.tank.move()

        self.bullets = [
            bullet
            for bullet in self.bullets
            if bullet.check_out_of_screen(self.size) is False
        ]

        for bullet in self.bullets:
            bullet.move()

    def check_collisions(self):
        """
        This checks whether any of the objects within the game have collided
        with each other. Specifically, we are looking for collisions between
        bullets and targets or the tank and targets
        """
        deletions = 0
        num_bullets = len(self.bullets)

        for i in range(num_bullets):
            for target in self.targets:
                if self.bullets[i - deletions].check_collision(target) is True:
                    a = self.bullets.pop(i - deletions)
                    del a
                    b = self.targets.pop(self.targets.index(target))
                    del b
                    self.playerscore += 20
                    deletions += 1
                    break

        for target in self.targets:
            if self.tank.check_collision(target) is True:
                a = self.targets.pop(self.targets.index(target))
                del a
                deletions += 1
                self.playerscore += 10  # only 10 for running over targets lol

        for i in range(deletions):
            a = Target(speed=[0, 0])
            a.moveto(
                (
                    random.randint(0, self.size[0] - a.size[0]),
                    random.randint(0, self.size[1] - a.size[1]),
                )
            )
            self.targets.append(a)

    def update_display(self):
        self.screen.fill(SANDBROWN)

        # tank
        self.tank.draw(self.screen, SANDBROWN)

        # targets
        for target in self.targets:
            target.draw(self.screen, BLACK)

        # bullets
        for bullet in self.bullets:
            bullet.draw(self.screen, BLACK)

        # score text
        font_img = self.font.render(
            "Score: %s" % str(self.playerscore), True, BLACK
        )
        font_rect = font_img.get_rect()
        pygame.draw.rect(self.screen, SANDBROWN, font_rect, 1)
        self.screen.blit(font_img, font_rect)


game = Tank_Game()
game.mainloop()
