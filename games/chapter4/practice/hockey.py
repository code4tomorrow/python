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

# please use the provided constants.


# Classes that should be in this file:
# Game_obj - an abstract base class for the Player and the Ball class
#       it should have an __init__, move, a moveto, and a check_collision
#       method. See their individual descriptions.
# Player - a class that represents one player. It should have a
#       __init__, draw, set_path, key_checker, and set_speed method. See
#       their individual descriptions
# Ball - a class that represents the ball. It should have a
#       __init__, draw, collide_line, get_paddle_collision_dir, get_obj_path,
#       collide_paddle, and trace_collisions method. See their individual
#       descriptions.
# BoundingLine - a class that represents the lines on the edges of the screen
#       Doesn't inherit from Game_obj. It should have a __init__ and
#       draw method.
# Goal - a class that inherits from BoundingLine. It should override
#       BoundingLine's draw method to draw its rectangle in white.
# App - an abstract class to provide the structure of the game.
# Hockey - the functional class whose mainloop will be called
#       to play hockey.


import pygame  # noqa: F401
from pygame import Rect
import math
import random

BLACK = (0, 0, 0)
GREEN = (0, 120, 0)
RED = (120, 0, 0)
WHITE = (255, 255, 255)

# initial screensize
SCREENSIZE = [900, 600]

# how big the ball's radius will be
BALL_RADIUS = 3


class Game_obj:
    def __init__(self):
        """
        This should just declare the variables
        later used in the other methods
        """
        self.speed = {"x": 0, "y": 0}
        self.rect = Rect

    def move(self):
        """
        This should move self.rect according to self.speed
        by using self.rect's move method as demonstrated in OOP_game.py.
        """
        pass  # your code here

    def moveto(self, coordinate):
        """
        This should move self.rect so that its top left lies at
        the provided coordinate.
        """
        pass  # your code here

    def check_collision(self, other):
        """
        This should return either True or False based on whether
        self.rect's collide_rect method returns 1 or 0 (respectively)
        similar to how it is done in OOP_game.py
        """
        pass  # your code here


class Player(Game_obj):
    PLAYERSPEED = (3, 3)
    PADDLESIZE = (10, 50)  # x width, y width

    def __init__(self, control_keys):
        """
        Creates a player rectangle. It should have an attribute
        self.control_keys from provided control keys. It should
        create a rectangle at (0, 0) that has self.PADDLESIZE dimensions.
        It should also initialize self.path to [0,0] (x_path, y_path)
        Arguments:
            control_keys - (dict) should be a dictionary of the following format:
                {
                "up": (KEY) (ex: K_w),
                "down": (KEY) (ex: K_s),
                "left": (KEY) (ex: K_a),
                "right": (KEY) (ex: K_d)
                }
        """
        pass

    def draw(self, surface: pygame.Surface):
        """
        This should draw self.rect onto the surface in the color GREEN
        """
        pass  # your code here

    def set_path(self, event):
        """
        This is the method that calls self.key_checker for 'up', 'down',
        'left', and 'right'
        """
        pass  # your code here

    def key_checker(self, event, direction):
        """
        This is the method that should do the actual work of checking whether
        the key pressed or let go in the event is in self.control_keys
        and whether the key pressed corresponds to the provided direction in
        self.control_keys
        Arguments:
            event - a pygame event
            direction (str) - either 'up', 'down', 'left', or 'right' (since those
            are the keys in self.control_keys)
        """
        pass  # your code here

    def set_speed(self):
        """
        Sets the speed according to the Player object's path.
        This should be called after self.path has been set.
        """
        # this is provided since it's math-intensive.
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

    def __init__(self, radius):
        """
        This should set up self.rect to a rectangle
        at (0, 0) and with height and width radius*2
        It should also set self.radius to the provided radius.
        Lastly, it should set an initial speed (provided)
        """
        # your code here

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

    def draw(self, surface: pygame.Surface):
        """
        This should use pygame.draw's builtin method for
        drawing circles to draw the ball onto the screen in
        white.
        """
        pass  # your code here

    def collide_line(self, other):
        """
        Checks if the ball has hit a line.
        If it did, update the speed accordingly

        Arguments:
            other (BoundingLine or Goal) - the line to check for a collision with
        Returns:
            True - if the collision happened
            False - if the collision didn't happen
        """
        pass  # your code here

    def get_obj_path(self, object: Game_obj) -> tuple:
        """
        if the object's speed is greater than 0, x_path = 1
        elif the object's speed is less than 0, x_path = -1
        else, the x_path = 0.
        Do the same for y speed for a variable y_path.
        """
        # your code here

        return  # (x_path, y_path) (uncomment when you write your code here)

    def get_paddle_collision_dir(self, paddle: Player) -> tuple:
        """
        Gets the direction in which the ball will be headed
        after a collision with a paddle.
        Does not actually check if the collision happened
        Provided since it's somewhat complicated

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
            15  # this is in degrees; it's just a fine-tuning aspect
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
            angle = random.randint(MINIMUM_ANGLE, int(math.pi / 2 * 100)) / 100

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

    def __init__(self, parameters):
        """
        Replace 'parameters' with real parameters.
        This should take:
            the starting coordinate of the line
            the ending coordinate of the line
            the line's name (which should either be
                'up', 'down', 'left', or 'right')
            (optional) default_size - the size of the line. If not provided,
                use DEFAULT_SIZE
        This should create the rectangle that stretches from the start
        coordinate to the end coordinate with a width or height
        (depending on its orientation) of default_size
        (or DEFAULT_SIZE if default_size isn't provided)
        """

    def draw(self, screen: pygame.Surface, color):
        """
        Draw self.rect onto the screen in the provided color, which should
        default to red.
        """
        pass  # your code here


class Goal:
    """
    This class should inherit from BoundingLine and should override the
    draw method to draw self.rect in white.
    """


class App:
    """
    This should be an abstract class to provide the structure of the game.
    If you need help starting, look at OOP_game.py for an example of
    how the App class should work. Keep in mind that you'll need
    "2 loops" within your mainloop because you'll need one that runs the game
    and one that displays the winning text after the game finished.
    """


class Hockey:
    """
    This is the functional class whose mainloop will be called
    to play hockey.
    This should inherit from App (where mainloop is defined)
    Its methods should utilize the methods within the
    game object classes.
    """

    def __init__(self):
        """
        This should initialize players, the ball, goals, and boundinglines
        (or, if you have a create_objects method, it should call that)
        """
        pass  # your code here

    def update_display(self):
        """
        This should fill the screen with BLACK and then
        use the draw method of each of the objects to draw them onto
        the screen.
        """
        pass  # your code here

    def move_objects(self):
        """
        This should use the move method for the players and the ball
        """
        pass  # your code here

    def check_events(self):
        """
        This should set the path for each of the players before setting
        their speed.
        """
        pass  # your code here

    def check_collisions(self):
        """
        This should check whether the ball collided with the goal, the
        bounding lines, or a player's paddle
        """
        pass  # your code here

    def display_winning_text(self):
        """
        This should fill the screen with BLACK, and display
        'Game Over. Player _ won' on the screen.
        """
        pass  # your code here


our_game = Hockey()
our_game.mainloop()
