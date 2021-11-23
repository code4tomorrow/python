from random import choice, randint

# how poker actually works:
# Every player is dealt two cards (face down)
# The number of cards in the middle (face up) is initially 3 and
# is increased one per round. Players decide if they want to bet on the round
# or fold before the next card is revealed. If a player bets, then all other
# players must 'call' (put in the same # of chips)
# once there are 5 cards in the middle, then the players see
# who can make the best match with their 2 cards and
# the 5 cards in the middle the player that makes the best match wins

# check the code in the area that says "--CODE AREA--"
# THERE ARE 4 INSTRUCTIONS; if you fill them out, then the program should work.
# Note that, in our version of poker, the game ends once any player has less
# than 7 chips.

suites = ["Clubs", "Diamonds", "Hearts", "Spades"]
face_cards = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
rankings = {
    0: "Royal Flush",
    1: "Straight Flush",
    2: "Four of a kind",
    3: "Full House",
    4: "Flush",
    5: "Straight",
    6: "Three of a Kind",
    7: "Two pairs",
    8: "Pair",
    9: "High Card",
}
deck = []

# --- SUPPORTING CODE ---
class card:
    def __init__(self, value: int, suite: str, name: str = None):
        self.name = name if name else str(value)
        self.value = value
        self.suite = suite

    def __str__(self) -> str:
        return f"A(n) {self.name} of {self.suite}"

    def __eq__(self, o) -> bool:
        return str(self) == str(o)

    def __sub__(self, o) -> bool:
        return self.value - o.value


class hand_results:
    """
    A class for easy comparing of results of a hand
    Note that a hand_result is considered "less than" another
    hand_result if the hand_result's priority has a lower value
    than the other hand_result's priority (meaning that
    the first hand_result has a higher priority). Vice versa for
    gt
    """

    def __init__(self, results: list):
        self.results = results
        self.priority = results.index(True) if True in results else len(results)

    def __lt__(self, o) -> bool:
        return self.priority > o.priority

    def __le__(self, o) -> bool:
        return self.priority >= o.priority

    def __gt__(self, o) -> bool:
        return self.priority < o.priority

    def __ge__(self, o) -> bool:
        return self.priority <= o.priority

    def __eq__(self, o) -> bool:
        return self.priority == o.priority


class hand:
    """
    This class represents one person's hand (or the river)
    """

    def __init__(self):
        self.cards = []

    def add_card(self, card: card) -> None:
        self.cards.append(card)

    def __str__(self) -> str:
        msg = ""
        for card in self.cards:
            msg += str(card) + ", "
        return msg

    def __len__(self) -> int:
        return len(self.cards)

    def union(self, o) -> None:
        for card in o.cards:
            self.cards.append(card)

    def does_val_card_exist(self, val: int, cards_not_equal_to: list = []) -> tuple:
        for card in self.cards:
            if card.value == val and card not in cards_not_equal_to:
                return (True, card)
        return (False, None)

    def find_matches(self, num_matches: int, cards_to_exclude: list = []) -> tuple:
        for card in self.cards:
            temp = []
            for oth in cards_to_exclude:
                temp.append(oth)
            if card not in temp:
                temp.append(card)

            for i in range(num_matches - 1):
                bool_val, potential_card = self.does_val_card_exist(card.value, temp)
                if not bool_val:
                    break
                temp.append(potential_card)
            else:
                card_matches = temp
                for oth_card in cards_to_exclude:
                    card_matches.remove(oth_card)
                return (True, card_matches)
        return (False, [])

    def check_straight_flush(self, card_start: card):
        potential_card = card_start
        for i in range(4):  # there need to be 4 cards higher than it
            bool_val, potential_card = self.does_val_card_exist(
                potential_card.value + 1
            )
            if not bool_val or potential_card.suite != card_start.suite:
                break
        else:  # for loop finished fine
            return True
        return False

    def check_straight(self, card_start: card) -> bool:
        potential_card = card_start
        for i in range(4):  # there need to be 4 cards higher than it
            bool_val, potential_card = self.does_val_card_exist(
                potential_card.value + 1
            )
            if not bool_val:
                break
        else:  # for loop finished fine
            return True
        return False

    def get_best_hand(self) -> hand_results:
        # try to get a 5 card flush:
        flush_possible = False
        for card in self.cards:
            same_suite = 0
            for other_card in self.cards:
                if not card == other_card and card.suite == other_card.suite:
                    same_suite += 1
            if same_suite >= 5:
                flush_possible = True

        # try to get a 5 card straight
        straight_possible = False
        for card in self.cards:
            potential_card = card
            for i in range(4):  # there need to be 4 cards higher than it
                bool_val, potential_card = self.does_val_card_exist(
                    potential_card.value + 1
                )
                if not bool_val:
                    break
            else:  # for loop finished fine
                straight_possible = True

        # try to get a straight flush
        straight_flush_possible = False
        if straight_possible and flush_possible:
            for card in self.cards:
                if not straight_flush_possible:
                    straight_flush_possible = self.check_straight_flush(card)

        # royal flush possible
        royal_flush_possible = False
        if self.does_val_card_exist(10)[0]:
            royal_flush_possible = self.check_straight(self.does_val_card_exist(10)[1])

        # try to get a pair (2 cards of same val)
        pair_possible = self.find_matches(2)[0]

        # try to get a 3 of a kind
        three_possible = self.find_matches(3)[0]

        four_possible = self.find_matches(4)[0]

        # try to get a full house
        full_house_possible = False
        for card in self.cards:
            bool_val, cards = self.find_matches(3)
            if (
                bool_val and not full_house_possible
            ):  # was able to find 3 of a kind (2 other cards of same value)
                # use exclude and try to find a pair
                full_house_possible = self.find_matches(2, cards)[0]

        two_pair_possible = False
        for card in self.cards:
            bool_val, cards = self.find_matches(2)  # find a pair
            if bool_val and not two_pair_possible:
                two_pair_possible = self.find_matches(2, cards)[0]

        return hand_results(
            [
                royal_flush_possible,
                straight_flush_possible,
                four_possible,
                full_house_possible,
                flush_possible,
                straight_possible,
                three_possible,
                two_pair_possible,
                pair_possible,
            ]
        )


def initialize_deck():
    global deck

    deck = [
        card(value, suite, face_cards[value]) if value >= 11 else card(value, suite)
        for value in range(2, 15)
        for suite in suites
    ]


def take_card() -> card:
    global deck
    c = choice(deck)
    deck.remove(c)
    return c


# -- CODE AREA --
# -- Your code will go here --

dealer_chips = 20
player_chips = 20


def play_poker():
    global dealer_chips, player_chips, deck

    round_num = 0
    player_inp = ""

    # INSTRUCTION
    # while both players have more than 7 chips
    while """YOUR CONDITION HERE""":
        initialize_deck()

        # inicialize hands to randomized ones each round
        player = hand()
        dealer = hand()
        river = hand()
        for i in range(2):  # two cards initially
            dealer.add_card(take_card())
            player.add_card(take_card())
        # initialize the pool in the middle
        for i in range(3):
            river.add_card(take_card())

        chips_at_stake = 0
        winner = ""

        round_num += 1
        print(f"round number {round_num}")
        # do one individual round
        while len(river) < 5:
            print(f"your hand right now is {player}")
            print(f"the river is currently {river}")
            # dealer bet
            dealerbet = min(
                randint(1, 5), dealer_chips
            )  # that way the dealer doesn't go into negative chips
            dealer_chips -= dealerbet
            chips_at_stake += dealerbet

            # player either calls or folds
            print(f"dealer bet {dealerbet}")
            player_inp = input(
                "call (bet that much) or fold (abandon this round) or STOP? "
            )

            # INSTRUCTION
            # handle input
            # if the input is 'STOP', then quit the program
            # if the input is 'call', then the player bets the same number
            # of chips that the dealer bet (player chips will decrease
            # and chips_at_stake will increase)
            # lastly, if the input is 'fold', then set winner to True
            # and break out of the round (use the break keyword)

            # update the river
            river.add_card(take_card())

            print(f"currently, dealer has {dealer_chips} chips")
            print(f"currently, you have {player_chips} chips")

            print()

        print(f"The river ended up as {river}")
        print()
        # no winner yet (meaning the round ended normally)
        if winner == "":
            # compare hands
            dealer.union(river)
            player.union(river)

            dealer_result = dealer.get_best_hand()
            player_result = player.get_best_hand()
            print(
                "It was your",
                rankings[player_result.priority],
                "vs the dealer's",
                rankings[dealer_result.priority],
            )

            # INSTRUCTION
            # if player_result is greater than or equal to
            # dealer_result, then the player won that round
            # if not, then the dealer won that round.
            # make sure to update the variable winner

        # INSTRUCTION
        # if the dealer won, then
        # print "The dealer won that round"
        # The dealer then gets the chips that were in chips_at_stake
        # if you won, then
        # print "You won that round"
        # the player gets the chips that were in chips_at_stake
        # chips_at_stake will be 0 again no matter what
        # Also, make sure to
        # print how many chips each player has
        print()  # used to make it look prettier since adds extra line


play_poker()
