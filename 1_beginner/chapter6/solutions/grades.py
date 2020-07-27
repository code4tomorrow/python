"""
Grades

Create a list called names and a list called grades.
Ask the user to input a name, and then ask
them to input the person's grade. Add the inputs
to the corresponding lists. Use a for loop to ask
for these inputs 5 times.

Display the info as "[name]: [grade]".

Example lists AFTER user input:
names = ["John", "Belle", "Ria", "Steph", "Louis"]
grades = [93, 85, 100, 82, 70]

Example output:
John: 93
Belle: 85
etc.
"""

names = []
grades = []

# Collect inputs.
for i in range(5):
    names.append(input("Enter a name: "))
    grades.append(input("Enter their grade: "))

# Format output correctly.
for i in range(len(names)):
    print(names[i] + ": " + grades[i])
