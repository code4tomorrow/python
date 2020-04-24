'''
Topics:
- string or number?
- data type conversion
'''

message = "Hello!"
z = '6'

x = '5' # this is a string
y = 5 # this is an integer

print(x + z) # this is not 11 because x and z are strings

a = 5 # this is an integer
b = 5.0 # this is a float

# converting data types
sum = int(x) + int(z) # this is 11 because x and z were converted to integers
print(sum)
number = str(b) # converts b to a string
print(message + " " + number) # string concatenation