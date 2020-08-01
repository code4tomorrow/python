"""
Capital

Write a program that takes a string as input,
makes every other letter capital, sets the rest
of the characters to be lowercase, and displays
the new string.

Hint: Make sure you don't count non-alphabetic
characters.

Example input: I love Zee the Cat.
Example output: I lOvE zEe ThE cAt.
"""

str = input("Enter a string: ")

new_str = ""
letter_count = 0  # Used to avoid counting non-alpha characters.

for c in str:
    if c.isalpha():
        if letter_count % 2 == 0:
            new_str += c.upper()
        else:
            new_str += c.lower()
        letter_count += 1
    else:
        new_str += c

print(new_str)
