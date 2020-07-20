# Create a class called Student with instance attributes: name and age.
# The user can input the name and age. Add 2 methods to the class:
# 1. A raise_hand method which prints out the student's name followed
# by "is now raising their hand."
# 2. A grow_older method that makes the student older by 1 year.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def raise_hand(self):
        print(self.name + " is now raising their hand.")

    def grow_older(self):
        self.age += 1
