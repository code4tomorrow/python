# Equals
# Write a program that takes an integer a from the user
# and turns it into a floating point number b. 
# Then, print b = a. For example, if the input 
# was 5, the program would print 5.0 = 5

# prompt user for an int
a = int(input("Enter an integer: "))

# convert to float
b = float(a)

# print both numbers
print(b, '=', a)