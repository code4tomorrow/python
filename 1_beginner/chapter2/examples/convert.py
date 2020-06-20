# Converting to Different Data Types

x = '5'
y = '6'
sum = int(x) + int(y) # this is 11 because x and y were converted to integers
print(sum)

a = 5
message = "Hello!"
a = str(a) # converts to string so that concatenation works
print(message + " " + a)

# print the type of a variable
a = 5
print(type(a)) # prints <class 'int'>