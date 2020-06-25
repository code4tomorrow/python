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

#See if you can write the same program, but without using >= anywhere
#This question is pretty tricky, so don't worry if you can't figure it out. We will go over it in class

#write code here
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
