'''
Ask the user for 4 numbers.
Use only 3 if else blocks to find
the largest number. You may not use elifs.
For example, this counts as an if/else block:

if 2 > 3:
    print("yay")
else:
    print("nay")

This question is really tricky, and requires some ingenuity.
'''

a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))
d = float(input("Enter number 4: "))

max_1 = -1
max_2 = -1
max_final = -1

if a > b:
    max_1 = a
else:
    max_1 = b

if c > d:
    max_2 = c
else:
    max_2 = d

if max_1 > max_2:
    max_final = max_1
else:
    max_final = max_2

print("The max is", max_final)
