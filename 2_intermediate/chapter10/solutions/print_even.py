# Solution 14
# Given the 2D list below, 
# print every element at an even index
# of each inner list. (Consider 0 to be even.)
# Hint: A special message should appear
# if you did it right!

my_list = [
    ['awesome', 'hello', 'job', 'world'],
    ['you', 'words', 'got', 'books'],
    ['it', 'python', 'right'],
    ['keep', 'plant', 'learning'],
    ['how', 'school', 'to'],
    ['code']
]

for words in my_list:
    for i in range(0, len(words), 2):
        print(words[i])