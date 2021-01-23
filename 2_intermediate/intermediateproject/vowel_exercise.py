words = ["Apple", "Orange", "Candles", "Kara", "orange"]

output = []
VOWEL_LIST = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
for elem in words:  # Loops through every element in words
    if len(elem) % 2 == 0 or elem[0] in VOWEL_LIST:
        num_vowels = 0
        for char in elem:
            if char in VOWEL_LIST:
                num_vowels += 1
        output.append(num_vowels)
    else:
        num_consonants = 0
        for char in elem:
            if char not in VOWEL_LIST:
                num_consonants += 1
        output.append(num_consonants)
print(output)  # Should print [2, 3, 5, 2, 3] in this case
