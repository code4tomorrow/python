"""
Replace

Write a Python program to print a string
from a given string where all occurrences
of its first char have been changed to '$',
except the first char itself.

Sample String: 'restart'
Expected Result: 'resta$t'

Adapted from W3Resource, problem 4:
https://www.w3resource.com/python-exercises/string/
"""

string = input("Enter a string: ")
first_char = string[0]

result = first_char

for i in range(1, len(string)):
    if string[i] == first_char:
        result += "$"
    else:
        result += string[i]

print(result)
