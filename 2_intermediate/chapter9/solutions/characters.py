# Characters
# Write a Python program to create
# a dictionary from a string where
# the keys are the characters
# and the values are the frequency
# of the characters.
#
# Your program should ask the user
# to enter a string, convert it into
# the dictionary described above,
# and print the resulting dictionary.
# 
# Example output:
# Enter a string: hello244oh
# {'h': 2, 'e': 1, 'l': 2, 'o': 2, '2': 1, '4': 2}

characters = {}
string = input("Enter a string: " )

for char in string:
    if char in characters:
        characters[char] += 1
    else:
        characters[char] = 1

print(characters)