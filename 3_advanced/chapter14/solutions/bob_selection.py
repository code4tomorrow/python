"""
Problem Name: bob_selection
Bob is choosing a person to go to the moon with him. The way he
chooses is quite strange. He will choose the first person from a
list given to him whose age is divisible by 5 and whose index
within the list is divisible by 5. If he does find such a person,
print the person’s name. If he doesn’t, don’t print anything. The
list given to him contains lists which contain the person’s name
and age. Use enumerate to solve this problem.
"""

# the list is given to him
people_list = [
    ("Ana", 22),
    ("Mark", 41),
    ("Dan", 10),
    ("Jack", 14),
    ("Ben", 51),
    ("Jorge", 65),
]

# write your code below
for index, person_data in enumerate(people_list):
    if person_data[1] % 5 == 0 and index % 5 == 0:
        print(person_data[0])
        break
