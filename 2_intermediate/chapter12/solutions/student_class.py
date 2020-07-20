# Create a class called Student with instance attributes: Name and Age.
# The user can input the Name and Age. Add 2 methods to the class:
# A raiseHand method which prints out the student name followed
# by “is now raising their hand.” A growOlder method that makes the
# student older by 1 year.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def raiseHand(self):
        print(self.name + " is now raising their hand.")

    def growOlder(self):
        self.age += 1
