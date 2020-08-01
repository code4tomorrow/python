"""
Every Other Word

Write a program that takes a sentence
as input and prints every other word.

Example input: I like cats, dogs, and pizza.
Example output:
I
cats,
and
"""

sentence = input("Enter a sentence: ")
words = sentence.split()
for i in range(0, len(words), 2):
    print(words[i])
