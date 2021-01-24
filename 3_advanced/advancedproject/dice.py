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
