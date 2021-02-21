import requests
import shelve


class game:
    def __init__(self, pageinfo, bsl: int, gns, gds, gps, gops, end):
        """
        Arguments:
          bsl is the beginning search location. It should be an integer
          pageinfo is the html of a website converted to a string
          gns is the 'game's name start'; it is what to look for directly
            before a game's name
          gds is the 'game's discount start'; it is what to look for directly
            before a game's discount
          gps is the 'game's price start'; it is what to look for directly
            before a game's discounted price
          gops is the 'game original price start'; it is what to look for
            directly before a game's original price

        """
        self.string = pageinfo
        self.isvalid = True
        self.begin = bsl
        self.endloc = 0

        self.discount = self.find(self.string, gds, end, cb=True)
        self.price = self.find(self.string, gps, end)
        self.ogprice = self.find(self.string, gops, end)
        self.name = self.find(self.string, gns, end, cwe=True)

    def find(self, string, start: str, end: str, cb=False, cwe=False):
        """
        Arguments
          string is the string where the substring you are looking for
            is located
          start is the substring directly before the substring you are
            looking for
          end is the substring directly after the substring you are
            looking for
          cb is whether or not to change the beginning point for the
            searches to the endloc
          cwe is whether to compare the endloc with self.begin and
            check whether the difference is withing the acceptable range
        """
        try:
            startloc = string.index(start, self.begin)
            endloc = string.index(end, startloc)
        except Exception:
            self.endloc = self.begin + 1
            self.isvalid = False
            return

        if cb:
            self.begin = endloc
        if cwe:
            # check if the  end location is too far away from the
            # beginning to be a valid name
            if endloc - self.begin > 300:
                self.isvalid = False
            self.endloc = endloc

        return string[startloc:endloc].lstrip(start).rstrip(end)


class scansteampage:
    def __init__(self, database="gameshelf"):
        """
        See game's explanation for the abbreviations
        """
        link = "https://store.steampowered.com/"
        gns = '<div class="tab_item_name">'
        gds = '<div class="discount_pct">-'
        gops = 'class="discount_original_price">'
        gps = 'class="discount_final_price">'
        end = "</div>"

        self.games = []
        self.database = database
        info = requests.get(link).text

        self.gather_games(info, gns, gds, gps, gops, end)
        self.write_info()

    def gather_games(self, info, gns, gds, gps, gops, end):
        """
        This method adds game objects to the scansteampage
        object's list self.games
        """
        position = 0
        consecutive_fails = 0

        while consecutive_fails < 2:
            a_game = game(info, position, gns, gds, gps, gops, end)
            position = a_game.endloc
            if a_game.isvalid:
                self.games.append(a_game)
                consecutive_fails = 0
            else:
                consecutive_fails += 1

    def write_info(self):
        """
        This method makes writes to the database.

        The database's keys will be games' titles
        The database's values will be strings of the following
          format:
            (name) is on sale for (price), which is a (discount percent)
            discount from its original price of (original price)
        """
        gameshelf = shelve.open(self.database)
        if len(gameshelf.keys()) > 0:
            gameshelf.clear()
        for game in self.games:
            gameshelf[game.name] = (
                "%s is on sale for %s, which is a %s"
                % (game.name, game.price, game.discount)
                + " discount from its original price of %s" % game.ogprice
            )
        gameshelf.close()


# comment out the below line after running it once
ourgamesshelf = scansteampage()

# The above code creates a shelf called gameshelf
# First, create a list to store the values
# Next, write "Current Sales\n" on a blank text file.
# Finally, write the values followed by 2 newlines to The
# text file.
# Your end result should look like below:
# Current Sales
# Something is on sale for $1000.00, which is a 50% discount from
# its original price of 2000.00

mygameshelf = shelve.open("gameshelf")
mytextfile = open("Sales!", "w")
mytextfile.write("Current Sales\n")
for value in mygameshelf.values():
    mytextfile.write(value + "\n\n")
mytextfile.close()
