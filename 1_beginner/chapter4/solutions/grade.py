"""
Grade
Write a program that asks the user to enter
the score for a student's test.
The letter grades are as follows:

A: >= 90
B: >= 80
c: >= 70
D: >= 60
F: < 60

Print the letter grade that the test score receives.
"""

score = float(input("Enter test score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

"""
See if you can write the same program,
but without using >= anywhere.
"""

score = float(input("Enter test score: "))
if score < 60:
    print("F")
elif score < 70:
    print("D")
elif score < 80:
    print("C")
elif score < 90:
    print("B")
else:
    print("A")
