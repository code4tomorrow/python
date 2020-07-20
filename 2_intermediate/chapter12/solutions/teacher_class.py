# Create a class called Teacher. Add 3 variables to this
# class: Name, Age, and an array of Student classes from student_class.
# The user can input these 3 variables. Add 2 Methods to the class: A
# displayClass method that prints out the names of all the students.
# A graduate method that increments the age of all of his/her students by 1.
# Then prints out all the ages.

# Student class implemented below. Teacher class uses it.

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def raiseHand(self):
        print(self.name + " is now raising their hand.")

    def growOlder(self):
        self.age += 1
        
class Teacher:

    def __init__(self, name, age, students):
        self.name = name
        self.age = age
        self.students = students

    def displayClass(self):
        for student in self.students:
            print(student.name)

    def graduate(self):
        for student in self.students:
            student.age += 1
            print(student.age)
    
