"""
Reverse Alphabet (Challenge Problem)

Create a list of strings by asking the user
to provide 10 inputs. Sort these in reverse
alphabetical order, and display the result.

Note: "Cat" will come before "dog" because of ASCII values.

To sort while IGNORING case, you might want to create
another list, make the elements all uppercase or all lowercase,
sort this list, and figure out how to use this list to
sort the original list.

"""

strings = []

# Get user input.
for i in range(10):
    strings.append(input("Enter a string: "))

# Create a lowercase version of strings.
lower_strings = []
for str in strings:
    lower_strings.append(str.lower())
lower_strings.sort()

# Set the position of each string in strings to the
# position of the lowercase string in lower_strings.
sorted_strings = strings.copy()
for str in strings:
    # i is the goal index of str.
    i = lower_strings.index(str.lower())
    sorted_strings[i] = str

# Display the sorted list.
print(sorted_strings)
