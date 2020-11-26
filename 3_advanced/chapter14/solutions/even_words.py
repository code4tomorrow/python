# Problem name: even_words
# Given a string that the user inputs create a list that contains the
# square of the lengths of words with an even amount of characters.
#
# For example, if the string is "I am cool", the list would be [4, 16].
# Use a list comprehension to solve it.

# The user inputs the string
string = input()

# write your code below
evenwords = [len(word) ** 2 for word in string.split() if len(word) % 2 == 0]
