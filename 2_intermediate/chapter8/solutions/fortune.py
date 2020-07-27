"""
Fortune

Store 6 fortunes cookie messages, and display a
random one each time the user runs the program.

Assume that you DON'T know how many messages are in the list.

(Hint: You’re randomly choosing the index to access.)
"""
import random

messages = [
  "You will meet the love of your life today.",
  "You will turn into a fish.",
  "It will rain diamonds today.",
  "You will encounter a field of mangoes.",
  "Look for the light. Underneath it, there will be a chess board.",
  "You'll run a sub-6:00 mile today."
]

print(messages[random.randrange(len(messages))])
