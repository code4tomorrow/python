# Make a two-player hockey game! The application will consist
# of two rectangular paddles, starting on each side of the screen,
# and one circular ball that players must bounce around. Players can
# move the paddles in any direction to hit the ball into the goal.
# If the ball makes contact with safe parts of the screen, it will
# bounce off at a random angle but in the same general direction
# (left or right). It will do the same if it makes contact with one
# of the paddles, but will head towards the opposite general direction
# instead. If the ball touches the goals on either side of the screen,
# the application will say “Game Over. Player _ Wins”. You must put
# your code in classes and have separate keys for each player to
# move their paddles.


import pygame
from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
    KEYUP,
    QUIT,
    RESIZABLE,
)
from pygame.rect import Rect

import math
import time
import random

# define the necessary color constants using rgb values
BLACK = (0, 0, 0)
GREEN = (0, 120, 0)
RED = (120, 0, 0)
WHITE = (255, 255, 255)

# define player controls
PLAYER1CONTROLS = {"up": K_w, "down": K_s, "left": K_a, "right": K_d}
PLAYER2CONTROLS = {
    "up": K_UP,
    "down": K_DOWN,
    "left": K_LEFT,
    "right": K_RIGHT,
}

# initial screensize
SCREENSIZE = [900, 600]

# how big the ball's radius will be
BALL_RADIUS = 3


class Game_obj:
    def __init__(self):
        # we don't want to pass actual values to the Rect class since
        # we want this class to be abstract
        self.rect = Rect
        self.prev_rect = Rect
        self.speed = {"x": 0, "y": 0}

    def move(self):
        self.prev_rect = self.rect
        self.rect = self.rect.move(self.speed["x"], self.speed["y"])

    def move_to(self, position: tuple):
        self.prev_rect = self.rect
        self.rect = self.rect.move(
            position[0] - self.rect.topleft[0],
            position[1] - self.rect.topleft[1],
        )

    def check_collision(self, other) -> bool:
        return self.rect.colliderect(other.rect) == 1


class Player(Game_obj):
    PLAYERSPEED = (3, 3)
    PADDLESIZE = (10, 50)  # x width, y width

    def __init__(self, control_keys: dict) -> None:
        """
        Creates a player rectangle with the provided control keys.
        Arguments:
            control_keys - (dict) should be a dictionary of the following format:
                {
                "up": (KEY) (ex: K_w),
                "down": (KEY) (ex: K_s),
                "left": (KEY) (ex: K_a),
                "right": (KEY) (ex: K_d)
                }
        """
        super().__init__()
        self.control_keys = control_keys
        self.rect = Rect(0, 0, self.PADDLESIZE[0], self.PADDLESIZE[1])
        self.path = [0, 0]

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, GREEN, self.rect)

    def set_path(self, event):
        if hasattr(event, "key") and event.key in self.control_keys.values():
            self.key_checker(event, "up")
            self.key_checker(event, "down")
            self.key_checker(event, "left")
            self.key_checker(event, "right")

    def key_checker(self, event: pygame.event.Event, direction: str) -> None:
        """
        Helper function to deal with event keys. Sets self.path
        according to PATH_VALUES
        Arguments:
            event(pygame.event.Event) - the event
            direction(str) - the direction to check KEYDOWN and KEYUP for.
        """
        PATH_VALUES = {"up": 1, "down": 1, "left": 0, "right": 0}
        DIRECTION_VALUES = {"up": -1, "down": 1, "left": -1, "right": 1}
        if event.key == self.control_keys[direction]:
            if event.type == KEYUP:
                self.path[PATH_VALUES[direction]] += -DIRECTION_VALUES[
                    direction
                ]
            if event.type == KEYDOWN:
                self.path[PATH_VALUES[direction]] += DIRECTION_VALUES[
                    direction
                ]

    def set_speed(self) -> None:
        """
        Sets the speed according to the Player object's path.
        This should be called after self.path has been set.
        """
        self.speed["x"] = (
            self.path[0]
            / math.sqrt(sum(abs(num) for num in self.path))
            * self.PLAYERSPEED[0]
            if (sum(abs(num) for num in self.path)) != 0
            else self.path[0] * self.PLAYERSPEED[0]
        )
        self.speed["y"] = (
            self.path[1]
            / math.sqrt(sum(abs(num) for num in self.path))
            * self.PLAYERSPEED[1]
            if (sum(abs(num) for num in self.path)) != 0
            else self.path[1] * self.PLAYERSPEED[1]
        )


class Ball(Game_obj):
    BALLSPEED = (6, 6)

    def __init__(self, radius: int) -> None:
        super().__init__()
        self.rect = Rect(0, 0, radius * 2, radius * 2)
        self.radius = radius

        # set up initial speed
        initial_ang = random.randint(1, int(math.pi / 2 * 100)) / 100
        self.speed["x"] = (
            math.cos(initial_ang)
            * self.BALLSPEED[0]
            * (-1 if random.randint(0, 1) == 0 else 1)
        )
        self.speed["y"] = (
            math.sin(initial_ang)
            * self.BALLSPEED[1]
            * (-1 if random.randint(0, 1) == 0 else 1)
        )

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen, WHITE, center=self.rect.center, radius=self.radius
        )

    def collide_line(self, other) -> bool:
        """
        Checks if the ball has hit a line.
        If it did, update the speed accordingly

        Arguments:
            other (BoundingLine or Goal) - the line to check for a collision with
        Returns:
            True - if the collision happened
            False - if the collision didn't happen
        """
        if self.check_collision(other):
            if other.name == "top" or other.name == "bottom":
                self.speed["y"] = -self.speed["y"]
                return True
            elif other.name == "left" or other.name == "right":
                self.speed["x"] = -self.speed["x"]
                return True
        return False

    def get_obj_path(self, object: Game_obj) -> tuple:
        if object.speed["x"] > 0:
            x_path = 1
        elif object.speed["x"] < 0:
            x_path = -1
        else:
            x_path = 0

        if object.speed["y"] > 0:
            y_path = 1
        elif object.speed["y"] < 0:
            y_path = -1
        else:
            y_path = 0

        return (x_path, y_path)

    def get_paddle_collision_dir(self, paddle: Player) -> tuple:
        """
        Gets the direction in which the ball will be headed
        after a collision with a paddle.
        Does not actually check if the collision happened

        Arguments:
            paddle (Player) - the player that the ball 'collided with'
        Returns:
            tuple(int, int) - a tuple of length 2 with just +-1's
                ex: (1, 1) or (1, -1) or (-1, 1), or (-1, -1)
                It corresponds to the direction in which the ball
                will be headed. The first item will be the x direction
                and the second item will be the y direction.
        """
        paddle_x_dir, paddle_y_dir = self.get_obj_path(paddle)

        ball_x_dir, ball_y_dir = self.get_obj_path(self)

        resulting_x_dir = None
        resulting_y_dir = None

        if paddle.speed["x"] == 0 or paddle_x_dir == ball_x_dir:
            if abs(paddle.speed["x"]) > abs(self.speed["x"]):
                resulting_x_dir = paddle_x_dir
            elif abs(paddle.speed["x"]) < abs(self.speed["x"]):
                resulting_x_dir = -ball_x_dir
        else:
            resulting_x_dir = -ball_x_dir

        if paddle.speed["y"] == 0 or paddle_y_dir == ball_y_dir:
            if abs(paddle.speed["y"]) > abs(self.speed["y"]):
                resulting_y_dir = paddle_y_dir
            elif abs(paddle.speed["y"]) < abs(self.speed["y"]):
                resulting_y_dir = -ball_y_dir
        else:
            resulting_y_dir = -ball_y_dir

        return (resulting_x_dir, resulting_y_dir)

    def collide_paddle(self, paddle: Player, executions: int) -> None:
        """
        Handles collisions with paddles.
        Arguments:
            paddle(Player) - the paddle to check for a collision with
            executions(int) - the amount of executions of the game's mainloop
                It's not important, but it prevents unwanted collisions during
                the 0th execution when we first set up the game by moving
                the objects to the right place
        """
        PROPORTION = 0.25  # used when "escaping" a collision
        MINIMUM_ANGLE = (
            30  # this is in degrees; it's just a fine-tuning aspect
        )
        # that makes the game more realistic

        resulting_x_dir = None
        resulting_y_dir = None

        a = self.trace_collisions(paddle)
        if a[0] and executions != 0:
            resulting_x_dir, resulting_y_dir = a[1]

        if self.check_collision(paddle):
            resulting_x_dir, resulting_y_dir = self.get_paddle_collision_dir(
                paddle
            )

        # if resulting_x_dir and resulting_y_dir aren't None, then update ball speed
        if resulting_x_dir and resulting_y_dir:
            print(MINIMUM_ANGLE * math.pi / 180 * 100)
            print(math.pi / 2 * 100)
            angle = (
                random.randint(
                    0,
                    int(
                        math.pi / 2 * 100
                        - (MINIMUM_ANGLE * math.pi / 180 * 100)
                    ),
                )
                / 100
            )

            print("angle", angle)

            self.speed["x"] = (
                math.cos(angle) * self.BALLSPEED[0] * resulting_x_dir
            )
            self.speed["y"] = (
                math.sin(angle) * self.BALLSPEED[1] * resulting_y_dir
            )

            # escape the collision so as to prevent the "same" collision from being
            # handled when collide_paddle is called next time.
            while self.check_collision(paddle):
                self.move_to(
                    (
                        self.rect.topleft[0] + PROPORTION * self.speed["x"],
                        self.rect.topleft[1] + PROPORTION * self.speed["y"],
                    )
                )

    def trace_collisions(self, paddle):
        COLLISIONS_TO_CHECK = 30  # the higher this is, the slower.

        # find how much the ball moved during the past execution
        delta_x = self.rect.topleft[0] - self.prev_rect.topleft[0]
        delta_y = self.rect.topleft[1] - self.prev_rect.topleft[1]

        # find how much the paddle moved during the past execution
        paddle_delta_x = paddle.rect.topleft[0] - paddle.prev_rect.topleft[0]
        paddle_delta_y = paddle.rect.topleft[1] - paddle.prev_rect.topleft[1]

        # check COLLISIONS_TO_CHECK times for a collision that occurred during
        # the "update game" phase (when we moved the objects)
        for i in range(COLLISIONS_TO_CHECK):
            # move both the ball and the paddle/player to where they would've been if we
            # subdivided the move phase into COLLISIONS_TO_CHECK individual frames
            ball_past = Ball(BALL_RADIUS)
            ball_past.move_to(
                (
                    self.prev_rect.topleft[0]
                    + (delta_x * i / COLLISIONS_TO_CHECK),
                    self.prev_rect.topleft[1]
                    + (delta_y * i / COLLISIONS_TO_CHECK),
                )
            )
            paddle_past = Player({})
            paddle_past.move_to(
                (
                    paddle.prev_rect.topleft[0]
                    + (paddle_delta_x * i / COLLISIONS_TO_CHECK),
                    paddle.prev_rect.topleft[1]
                    + (paddle_delta_y * i / COLLISIONS_TO_CHECK),
                )
            )

            # now that we have a ball and a paddle, check if they collided
            if ball_past.check_collision(paddle_past):
                return (True, ball_past.get_paddle_collision_dir(paddle_past))
        # if the loop failed (didn't return), then
        # return False and an empty tuple
        return (False, tuple())


class BoundingLine:
    DEFAULT_SIZE = 3

    def __init__(
        self,
        start_coord: tuple,
        end_coord: tuple,
        name: str,
        default_size=None,
    ):
        if default_size:  # if a default size is provided
            self.DEFAULT_SIZE = default_size

        self.start_coord = start_coord  # starting coordinate, normally topleft
        self.end_coord = end_coord  # ending coordinate, normally bottomright

        self.rect = Rect(
            start_coord[0],
            start_coord[1],
            end_coord[0]
            if end_coord[0] - start_coord[0] != 0
            else self.DEFAULT_SIZE,
            end_coord[1]
            if end_coord[1] - start_coord[1] != 0
            else self.DEFAULT_SIZE,
        )

        self.name = name  # this comes in handy in Ball's collide_line method

        # small fix for bottom and right bounding lines getting drawn outside of
        # the screen
        if self.name == "bottom" and self.rect.bottom > SCREENSIZE[1]:
            self.rect = self.rect.move(0, -3)
        elif self.name == "right" and self.rect.right > SCREENSIZE[0]:
            self.rect = self.rect.move(-3, 0)

    def draw(self, screen: pygame.Surface, color=RED):
        pygame.draw.rect(screen, color, self.rect)


class Goal(BoundingLine):
    def draw(self, screen: pygame.Surface):
        super().draw(
            screen, WHITE
        )  # the goal should be in white so you can see it


class App:
    def __init__(
        self, flags=RESIZABLE, width=900, height=600, title="My game"
    ):
        pygame.init()
        self.size = [width, height]
        self.screen = pygame.display.set_mode(self.size, flags)
        pygame.display.set_caption(title, title)
        self.running = True

        self.GAMESTATE = 0
        self.WONSTATE = 1
        self.QUITSTATE = 2

        self.currstate = self.GAMESTATE
        self.winning_player = 0  # will be 1 or 2 when a player won

        self.executions = 0  # useful for debugging

    def mainloop(self):
        while self.running:
            # main game loop (for the game itself)
            # because this is a while loop, the game will keep going until someone won
            # so we don't need to worry about the post-game text being displayed
            if self.currstate == self.GAMESTATE:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        # set the variables that are keeping the game running
                        # to values that won't keep the game running
                        self.running = False
                        self.currstate = self.QUITSTATE
                    else:
                        self.check_events(event)
                self.check_collisions()
                self.move_objects()
                self.update_display()
                pygame.display.update()
                time.sleep(0.01)
                self.executions += 1

            if self.currstate == self.WONSTATE:
                # 'post-game' game loop (just shows winning text)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.running = False
                        self.currstate = self.QUITSTATE
                self.display_winning_text()

            if self.currstate == self.QUITSTATE:
                pygame.quit()

    def check_events(self, event) -> None:
        pass

    def check_collisions(self) -> None:
        pass

    def move_objects(self) -> None:
        pass

    def update_display(self) -> None:
        pass

    def display_winning_text(self) -> None:
        pass


class Hockey(App):
    def __init__(self):
        super().__init__(title="Hockey!")

        # initialize players
        self.player_1 = Player(PLAYER1CONTROLS)
        self.player_2 = Player(PLAYER2CONTROLS)

        # move players to starting positions
        self.player_1.move_to(
            (
                self.size[0] / 8 - self.player_1.rect.width,
                self.size[1] / 2 - self.player_1.rect.height,
            )
        )
        self.player_2.move_to(
            (
                self.size[0] / 8 * 7 - self.player_2.rect.width,
                self.size[1] / 2 - self.player_2.rect.height,
            )
        )

        # initialize ball and move it to starting position (center)
        self.ball = Ball(BALL_RADIUS)
        self.ball.move_to(
            (
                self.size[0] / 2 - self.ball.rect.width,
                self.size[1] / 2 - self.ball.rect.height,
            )
        )

        # initialize bounding lines - the edges of the screen off which the
        # ball should bounce
        self.top_line = BoundingLine((0, 0), (self.size[0], 0), "top")
        self.bottom_line = BoundingLine(
            (0, self.size[1]), (self.size[0], self.size[1]), "bottom"
        )
        self.left_line = BoundingLine((0, 0), (0, self.size[1]), "left")
        self.right_line = BoundingLine(
            (self.size[0], 0), (self.size[0], self.size[1]), "right"
        )
        self.bounding_lines = [
            self.top_line,
            self.bottom_line,
            self.left_line,
            self.right_line,
        ]

        # initialize Goals
        self.goal_1 = Goal(
            (0, (self.size[1] / 2) - (5 * self.size[1] / 16)),
            (0, (self.size[1] / 2) + (self.size[1] / 16)),
            "left",
            3,
        )
        self.goal_2 = Goal(
            (self.size[0], (self.size[1] / 2) - (5 * self.size[1] / 16)),
            (self.size[0], (self.size[1] / 2) + (self.size[1] / 16)),
            "right",
            3,
        )

    def update_display(self) -> None:
        self.screen.fill(BLACK)  # fill the screen with black to clear it

        # draw main objects
        self.player_1.draw(self.screen)
        self.player_2.draw(self.screen)
        self.ball.draw(self.screen)

        # draw bounding lines
        self.top_line.draw(self.screen)
        self.bottom_line.draw(self.screen)
        self.left_line.draw(self.screen)
        self.right_line.draw(self.screen)

        # draw goals
        self.goal_1.draw(self.screen)
        self.goal_2.draw(self.screen)

    def move_objects(self) -> None:
        self.player_1.move()
        self.player_2.move()
        self.ball.move()

    def check_events(self, event) -> None:
        self.player_1.set_path(event)
        self.player_2.set_path(event)

        self.player_1.set_speed()
        self.player_2.set_speed()

    def check_collisions(self) -> None:
        for line in self.bounding_lines:
            self.ball.collide_line(line)
        self.ball.collide_paddle(self.player_1, self.executions)
        self.ball.collide_paddle(self.player_2, self.executions)

        if self.ball.collide_line(self.goal_1):
            self.currstate = self.WONSTATE
            self.winning_player = 2  # player 2 (right player) scored
        elif self.ball.collide_line(self.goal_2):
            self.currstate = self.WONSTATE
            self.winning_player = 1  # player 1 (left player) scored

    def display_winning_text(self) -> None:
        self.screen.fill(BLACK)

        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
        if self.winning_player != 0:
            font_img = self.font.render(
                "Game Over. Player %s won" % str(self.winning_player),
                True,
                WHITE,
            )
        else:
            # this won't actually be seen, but it prevents "Player 0 won" from showing
            # up on the screen for a split-second if QUIT was pressed before someone won
            font_img = self.font.render("Nobody won", True, WHITE)
        font_rect = font_img.get_rect()
        pygame.draw.rect(self.screen, BLACK, font_rect, 1)
        self.screen.blit(font_img, font_rect)
        pygame.display.update()  # show the new text.


our_game = Hockey()
our_game.mainloop()
