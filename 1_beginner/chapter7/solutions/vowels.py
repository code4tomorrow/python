'''
Vowels

Create a program which takes a string
from the user and prints the number
of vowels that are in the string.
'''
VOWELS = 'aeiou'

# Ask user for a string
string = input('Enter a string: ')

# Count the number of vowels in the string
number_of_vowels = 0
for char in string:
    if char in VOWELS:
        number_of_vowels += 1

# Print number of vowels
print('Number of vowels:', number_of_vowels)
