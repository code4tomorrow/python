# Grade
# Write a program that asks the user to enter
# the score for a student's test. 
# Print the letter grade that the test score receives.

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