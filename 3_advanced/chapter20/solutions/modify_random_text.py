# Create a program that creates a blank text file and writes a
# random number (in the form of a string) between 1 and 1000 on it.
# Next, close the file. Next, open the file again (this time read it)
# and read the text. Assign a variable to that data.
# print (not write) the variable, then print the int(variable) * 4.

import random

myfile = open("blank.txt", "w")
myfile.write(str(random.randint(0, 1000)))
myfile.close()

refile = open("blank.txt", "r")
thetext = refile.read()
print(thetext)
print(int(thetext) * 4)
