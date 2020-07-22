"""
Replace

Write a Python program that asks the user for a string
and then prints a version of that string
where all occurrences of its first char
have been changed to '$',
except the first char itself.

Sample Input: 'restart'
Expected Output: 'resta$t'

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
