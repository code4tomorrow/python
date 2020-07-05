'''
First Three Words

Write a program which asks
the user to enter a sentence.
Print the first three words in the sentence.
(Assume the user enters at least 3 words.)
'''

sentence = input('Enter a sentence: ')

words = sentence.split()

for word in words[:3]:
    print(word)
