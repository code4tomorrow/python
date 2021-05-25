# "w" stands for "write"
myfile = open("mytext.txt","w")

# "r" stands for "read"
myfile = open("mytext.txt","r")

# "a" stands for "append"
myfile = open("mytext.txt","a")


# writes into a mytext.txt
# "hello worldhi again"
myfile.write('hello world')
myfile.write('hi again')


# takes data from mytext.txt and prints it
mydata = myfile.read()
print(mydata)


# saves file
myfile.close()
