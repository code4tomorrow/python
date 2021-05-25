# String Manipulation

# immutable
name = "Ahsoka Tano"
# this does not change "Ahsoka Tano",
# it's assigning name to a different string
name = "Rey"

# string methods
message = "hey dude"
print(message)  # prints "hey dude"
message = message.upper()
print(message)  # prints "HEY DUDE"

message = "THIS WAS IN ALL CAPS"
print(message)  # prints "THIS WAS IN ALL CAPS"
message = message.lower()
print(message)  # prints "this was in all caps"

message = "one two three four five"
# prints ['one', 'two', 'three', 'four', 'five']
print(message.split())

message = "tahiti, it's, a, magical, place"
# prints ['tahiti', " it's", ' a', ' magical', ' place']
print(message.split(","))

message = "hello"
print(message.isalpha())  # True
message = "12345"
print(message.isalpha())  # False

message = "12345"
print(message.isdigit())  # True
message = "hello world"
print(message.isdigit())  # False

message = "   lots of white space     "
print(message)
message = message.strip()
print(message + "|")

# string indexing
my_string = "hello"
print(my_string[2])  # prints 'l'
print(my_string[2:4])  # prints 'll'
print(my_string[-1:-3:-1])  # prints 'ol'

for char in my_string:
    print(char)  # prints each character on its own line
