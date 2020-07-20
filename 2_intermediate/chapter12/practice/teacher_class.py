# Create a class called Teacher. Add 3 instance variables to this
# class: name, age, and students (a list of Student objects).
# Add 2 Methods to the class: A display_students method that
# prints out the names of all the students, each on their own line, and
# a graduate_students method that increments the age of all of the
# teacher's Students by 1. Then it should print out all their ages.

# Student class implemented below. Teacher class uses it.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def raise_hand(self):
        print(self.name + " is now raising their hand.")

    def grow_older(self):
        self.age += 1
