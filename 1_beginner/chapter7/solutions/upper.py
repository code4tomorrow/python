# Upper
# Continuously ask a user to enter words.
# You should remove leading/trailing whitespace, and then
# make sure that the word is only made up of letters.
# Store the words in a list.
# Stop asking the user for words if they enter an empty string
# (the string has no characters or is completely whitespace).
# Convert all of the words in the list into uppercase.
# Print the resulting list. (If the user quits right away,
# print an empty list.)

words = []

while True:
    word = input("Enter a word, or press enter to quit: ").strip()
    if word == "":
        break
    if word.isalpha():
        words.append(word.upper())
    else:
        print("Error, please enter 1 word")

print(words)
