"""
Lunch Tables
Ask the user to input how many people are in the lunchroom, 
and how many people can sit at each table.
Output the number of people that will be left without a table.
"""

# Get user input
people = input("How many people are in the lunchroom? ")
table_limit = input("How many people can sit at a table? ")

# Calculate the number of outcasts (the remainder)
outcasts = int(people) % int(table_limit)

# Display output
print("Outcasts:", outcasts)
