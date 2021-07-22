# Directions: The goal of blackjack is to be the first player
# to get to 21. Each player will draw randomly and the
# sum of the cards will add to 21.

import random


print("Welcome to the game of BlackJack. ")
print("")

# Create the lists of the two players
# the dealer is the console and the player is the user
dealerList = []
userList = []

# append two random cards to start the game
for i in range(2):
    dealerList.append(random.randint(2, 11))
    userList.append(random.randint(2, 11))
# print the first two cards
print("Here is the dealer's cards:" + str(dealerList))
print("Here is the user's cards:" + str(userList))
if sum(userList) == 21:
    print("User Won")
    exit()
if sum(dealerList) == 21:
    print("Dealer won")
    exit()

# ask hit or stay... write a functionn for hit and stay...
# conditional for the typed in key hit means to take another
# card and stay means to play with already drawn cards

# print the instructions
ask = input("Type in H to hit and S to stay:")


# write a function for hit to use in multiple scenarios
def hit(cards):
    cards.append(random.randint(2, 11))


# while loop will keep checking the two players' cards to see if they reached 21 or not
while ask == "H" or ask == "h":
    hit(userList)
    print("Here is your hand:" + str(userList))

    if sum(userList) > 21:
        print("User is Busted")
        exit()
    if sum(userList) == 21:
        print("User Won")
        exit()
    ask = input("Type in H to hit and S to stay:")

# if statement for "stay"
if ask == "S" or ask == "s":
    print("Here is your hand:" + str(userList))


# when hit- append a anotehr random number into the list of the dealer/userList
# when stay- just go to next play and print out the list
# while dealer less than 17 append new cards to the list

while sum(dealerList) < 17:
    hit(dealerList)
    print("Here is dealer's hand:" + str(dealerList))

# compare cards for win
if sum(dealerList) > 21:
    print("Dealer is Busted")

    exit()
if sum(dealerList) == 21 and sum(userList) == 21:

    print("It is a tie")
    exit()
if sum(dealerList) == 21:
    print("Dealer Won")
    exit()

if 21 - sum(dealerList) > 21 - sum(userList):
    print("User is closer")
if 21 - sum(dealerList) < 21 - sum(userList):
    print("Dealer is closer")
