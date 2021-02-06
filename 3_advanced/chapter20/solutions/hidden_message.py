# This problem uses the textfile.txt

myfile = open("./blank.txt", "r")
text = myfile.read().split()
myfile.close()
 
myfile = open("./blank.txt", "a")
myfile.write("\n\n")
for i in range(len(text)):
    if i % 7 == 0:
        myfile.write(text[i] + " ")
myfile.close()
