# List comprehensions are a faster and more
# elegant way to create a new list
# based on an existing list


# squares each number from 0 to 9 and adds to 'listL'
listL = []
for i in range(10):
    listL.append(i * i)
print(listL)
# prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# does the same thing as above, but in shorter, cleaner code
squares = [i * i for i in range(10)]
print(squares)
# also prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# squares all numbers in list 'a' IF they are greater than 5
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [i * i for i in a if i > 5]
print(squares)
# prints [36, 49, 64, 81, 100]


# converts all letters in 'word' to uppercase and adds to list 'ask'
word = " Hey how are you"
asks = [i.upper() for i in word]
print(asks)
# prints [' ', 'H', 'E', 'Y', ' ', 'H', 'O', 'W',
# ' ', 'A', 'R', 'E', ' ', 'Y', 'O', 'U']
