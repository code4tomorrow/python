"""
Names

Make a list called people and fill it with
at least 6 names. Make another list and use
list slicing to fill it with every other name
from the original list, starting with the 1st name.
Print both lists.
"""

people = ["Mark", "Anya", "Wan", "Jewel", "Stef", "Hank"]

# Answers may vary.
# Some other possible answers:
# group = people[0, 5, 2] or people[0, len(people), 2]

group = people[0:len(people):2]

print(people)
print(group)

"""
Use a for loop to ask the user to add 4 names
to the list. After you ask for each name, print
out the last 5 names of the list.
"""

for i in range(4):
    people.append(input("Enter a name: "))
    print("Last 5 names:", people[-5:])
