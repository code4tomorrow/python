# Daniel likes to get together with his friends every week on a
# random day to play dice. In his game of dice, the objective is
# to see who gets three of the same number first.

# Algorithm Description: Use a class to represent a player. Create a
# turn log (using 2d list with each inner list containing the outcomes
# for all players representing a turn. Ex: [[1,2,4],[4,2,6]] ).
# Create a dictionary (that is an instance variable of the player
# class) to keep track of how many of each dice outcome each
# person playing the game got. For example, Daniel’s outcomes can
# look like {1:2, 2:3, 3:1, 4:0, 5:1, 6:2}. Once a person gets 3
# of the same outcome, a unique statement will be created
# (the statement should be like "Player x won").
# If multiple people won, it should be like "Player x, y won"

# Follow these steps to create this algorithm.
# 1) Import the random module which we will be using later.

# 2) Create a main class with
# --- an init function that asks the user for how many
# players and creates that many player classes
# --- instance variable: holding a turn log that should take
# each player's result each round (see above)
# --- a 'round' method that simulates one round of the game

# 3) Create a player class with
# --- instance variable: holding a dictionary that stores how many
# times they got each outcome
# --- instance variable: that tracks whether the
# player has rolled 3 of the same thing(in other words won) or not.
# --- a 'roll' method that outputs a random int between 0 and
# 6 inclusive

import random


class main:
    def __init__(self):
        self.playercount = int(input("How many players are playing?  "))
        self.turnlog = []
        self.players = [player() for i in range(self.playercount)]
        self.winners = []
        self.over = False

        print(
            "Note: player 0 is the first player, "
            + "player 1 is the second player, etc"
        )
        while not self.over:
            self.round()
        print("This is the record of the game")
        print(self.turnlog)
        print("Player(s)", str(self.winners).lstrip("[").rstrip("]"), "won")

    def round(self):
        for i in range(self.playercount):
            self.players[i].roll()
            if self.players[i].win:
                self.winners.append(i)
                self.over = True
        self.turnlog.append(
            [self.players[x].thisround for x in range(self.playercount)]
        )


class player:
    def __init__(self):
        self.thisround = None
        self.outcomes = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        self.win = False

    def roll(self):
        self.thisround = random.randint(1, 6)
        self.outcomes[self.thisround] += 1
        if 3 in self.outcomes.values():
            self.win = True


letsplay = main()
