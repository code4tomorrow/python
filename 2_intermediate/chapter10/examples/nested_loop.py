# Nested Loops

# Traversing 2D Lists
my_list = [
    ["hello", "world", "code"],
    ["docs", "slides", "sheets"],
    ["google", "amazon", "facebook"],
    ["this", "is", "python"],
]

# print each element in my_list
# and each element in the inner lists
for inner_list in my_list:
    print(inner_list)
    for word in inner_list:
        print(word)
