import random

myfile = open("blank.txt", "w")
myfile.write(str(random.randint(0, 1000)))
myfile.close()

refile = open("blank.txt", "r")
thetext = refile.read()
print(thetext)
print(int(thetext) * 4)
