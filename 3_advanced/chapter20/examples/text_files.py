# The functions below are the basics of
# creating, editting, and reading text files.


# "a" stands for "append"
myfile = open("mytext.txt", "a")


# "w" stands for "write"
myfile = open("mytext.txt", "w")


# writes into a mytext.txt
# "hello worldhi again"
myfile.write("hello world")
myfile.write("hi again")


# saves file
myfile.close()


# "r" stands for "read"
myfile = open("mytext.txt", "r")


# takes data from mytext.txt and prints it
mydata = myfile.read()
print(mydata)
