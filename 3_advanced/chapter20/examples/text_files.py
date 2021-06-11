# The functions below are the basics of
# creating, editting, and reading text files.


# "a" stands for "append"
myfile = open("mytext.txt", "a")


# "w" stands for "write"
myfile = open("mytext.txt", "w")


# writes into a mytext.txt on different lines
# "hello world\nhi again\nhelloooo"
# You need to use the "\n" character if you want to write to a new line; if you
# don't use it, the next .write() will write to the same line as the previous .write()
myfile.write("hello world\n")  # writes on line 1
myfile.write("hi again\n")  # writes on line 2
myfile.write("helloooo")  # writes on line 3


# saves file
myfile.close()


# "r" stands for "read"
myfile = open("mytext.txt", "r")


# takes data from mytext.txt and prints it
mydata = myfile.read()
print(mydata)


# determines if myfile is readable
print(myfile.readable())


print(myfile.readline())  # prints the first line
print(myfile.readline())  # prints the second line
print(myfile.readline())  # prints the third line


# determines if you can set your position in myfile
print(myfile.seekable())


# sets your position to the 0th index
myfile.seek(0)


# prints a list of all the lines in the file
print(myfile.readlines())


# prints your position in a file
print(myfile.tell())


# determines if you can write into myfile
print(myfile.writable())


myfile = open("mytext.txt", "w")


# writes lines from provided list into myfile
myfile.writelines(["line one\n", "line 2"])


myfile.close()
