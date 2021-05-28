# Create a program that reads textfile.txt and writes (appends) 2
# newlines and then every 7th word followed by a space

# ex: given “hi”, “ho”, “ha”, “hy”, “he”, “hu”, “we”, “everyone”
# it would print 2 newlines and then ‘hi everyone’

myfile = open("./textfile.txt", "r")
text = myfile.read().split()
myfile.close()

myfile = open("./textfile.txt", "a")
myfile.write("\n\n")
for i in range(len(text)):
    if i % 7 == 0:
        myfile.write(text[i] + " ")
myfile.close()
