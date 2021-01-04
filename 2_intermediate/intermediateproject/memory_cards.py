import random


class memcards:
    def __init__(self, items: dict):
        self.memorder = [None for i in range(len(items) * 2)]
        self.dict = items
        self.keys = list(items.keys())
        self.values = list(items.values())
        self.shuffle()
        self.currmap = self.definemap()
        self.play()

    def play(self):
        instructions = (
            "The Rows and Columns start at 0, not 1; # means "
            + "unflipped; _ means correct"
        )
        # I used a set, but you could also have used a list or
        # a dictionary so long as you checked if elements were already
        # in the list before adding them
        flipped = set()
        print(instructions)
        while len(self.memorder) > len(flipped):
            self.display()
            row1 = int(input("Which row would you like to select?  "))
            column1 = int(input("Which column would you like to select?  "))
            item1 = self.flip(row1, column1, "reveal")
            row2 = int(input("Which row would you like to select now?  "))
            column2 = int(input("Which column would you like to select?  "))
            item2 = self.flip(row2, column2, "reveal")
            if item1 in self.dict and self.dict[item1] == item2:
                print("Correct!")
                flipped.add(self.flip(row1, column1, "correct"))
                flipped.add(self.flip(row2, column2, "correct"))
            elif item2 in self.dict and self.dict[item2] == item1:
                print("Correct!")
                flipped.add(self.flip(row1, column1, "correct"))
                flipped.add(self.flip(row2, column2, "correct"))
            else:
                self.flip(row1, column1, "hide")
                self.flip(row2, column2, "hide")
                print("Try again, incorrect  :(")
        print("Congratulations, you win! You found all of the pairs!")

    def definemap(self):
        # figure out potential heights and widths
        divisors = []
        for i in range(len(self.memorder)):
            if (len(self.memorder)) % (i + 1) == 0:
                divisors.append(i + 1)
        # gets the real width and height of map
        width = divisors[len(divisors) // 2]
        height = divisors[(len(divisors) // 2) - 1]
        themap = [["#  " for i in range(width)] for i in range(height)]
        return themap

    def shuffle(self):
        doneitems = {}
        while len(self.memorder) > len(doneitems):
            itemloc = random.randint(0, len(self.keys) - 1)
            b = random.randint(0, 1)
            memorderloc = random.randint(0, len(self.keys * 2) - 1)
            if memorderloc not in doneitems.values():
                if b == 0 and self.memorder[memorderloc] not in self.keys:
                    self.memorder[memorderloc] = self.keys[itemloc]
                    doneitems[self.memorder[memorderloc]] = memorderloc
                if b == 1 and self.memorder[memorderloc] not in self.values:
                    self.memorder[memorderloc] = self.values[itemloc]
                    doneitems[self.memorder[memorderloc]] = memorderloc

    def flip(self, row, column, operation):
        if operation == "reveal":
            self.currmap[row][column] = self.memorder[
                (row * len(self.currmap[0])) + column
            ]
            self.display()
            return self.memorder[(row * len(self.currmap[0])) + column]
        if operation == "hide":
            self.currmap[row][column] = "#  "
            return None
        if operation == "correct":
            self.currmap[row][column] = "_  "
            return self.memorder[(row * len(self.currmap[0])) + column]

    def display(self):
        for i in range(len(self.currmap)):
            print(self.currmap[i])


mydiction = {"a": 1, "b": 2, "c": 3}

letsplay = memcards(mydiction)
