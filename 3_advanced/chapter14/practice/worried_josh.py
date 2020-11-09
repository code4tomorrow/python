# Problem Name: worried_josh

"""

Josh is worried about his test score. He wants to score in the top n, 
where n is a positive integer that the user inputs. Given a list of 
student names where the student with the highest score is the 0th index 
and the score goes down from there, print “YES!” if Josh scores in the top n, 
and “NO :(“ if he doesn’t. Assume n will not be greater than the number of students. 
Use enumerate to solve this problem.

"""

# the list of student names is given and the n is a user input
# remember the leftmost student = highest score, rightmost student = lowest score
students = [“Dan”, “Sherlocks”, “Jo”, “Josh”, “Dennis”, “Erwin”, “Ivan”, “Penny”] 
n = int(input())

# write your code below
