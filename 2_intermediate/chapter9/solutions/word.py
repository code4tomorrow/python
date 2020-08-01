"""
Word

Store words (keys) and definitions (values)
in a dictionary in a random order.

Then, ask the user to input a word.
If the word is in the dictionary,
use it to display the definition.
Otherwise, print out a message saying
that the word is not there.

Display the entire dictionary at the end in the format:
word1: definition1
word2: definition2
etc.
"""

dictionary = {
    "monkey": "a cute human",
    "banana": "sustenance for cute humans",
    "neha": "a really strange human",
    "phone": "magic communication device",
    "cookie": "heaven on Earth",
}

# Show definition
word = input("Enter a word: ")
if word in dictionary:
    print("Definition:", dictionary.get(word))
else:
    print("This word cannot be found.")
print()

# Display formatted dictionary
for key, value in dictionary.items():
    print(key + ": " + value)
