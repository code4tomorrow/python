"""
Names

Write a program that asks a user
for two names, and outputs True if
the names are NOT the same.
"""

name1 = input("Person 1: ")
name2 = input("Person 2: ")

# "False" if name1 and name2 are equal
not_same = name1 != name2

print("Not the same?", not_same)
