# Consider a dice game played between 3 friends. The game consists of 5
# rounds, in which each player takes turns rolling a die numbered from 1-6.
# The friends are interested in dice and want to record their game using a
# Python program.

# Player Class

# Create a Player class to represent a friend. The __init__ method should 
# initialize 2 instance variables current and outcomes. current represents
# the player’s most recent roll. outcomes is a dictionary which will store
# a record of the player’s rolls, where the keys are the possible outcomes
# of each roll and the values are the number of times the player rolled that
# number. For example, outcomes[3] represents how many times the player rolled
# a 3.

# The roll method in this class should update current with a random dice outcome.
# It should also update the instance variable containing the dictionary. 

# Game Class

# Create a Game class that will simulate the entire dice game. The __init__ method
# should initialize 2 instance variables turn_log and players. turn_log is a list
# that has 5 elements (which are also lists) which represent each round. players
# is a list of Player objects representing the 3 friends.

# The round method will simulate a round in which all the players roll the dice
# once and turn_log is updated.

# The play method will simulate 5 rounds and also print results of the game.
# Specifically, the method will print the turn log and outcomes of each player.

# Hint: Import the random module.


import random


class main:
    def __init__(self):
        self.turnlog = []
        self.players = [player(), player(), player()]

        for i in range(5):
            self.round()

        print("Turn Log: " + str(self.turnlog))
        print()
        player_num = 1
        for player_a in self.players:
            print("Player " + str(player_num) + " :" + str(player_a.outcomes))
            player_num += 1

    def round(self):
        for i in range(3):
            self.players[i].roll()
        self.turnlog.append([self.players[x].thisround for x in range(3)])


class player:
    def __init__(self):
        self.thisround = None
        self.outcomes = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    def roll(self):
        self.thisround = random.randint(1, 6)
        self.outcomes[self.thisround] += 1


letsplay = main()
