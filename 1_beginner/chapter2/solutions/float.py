# Float
# Write a program that takes an integer from the user and turns it into a floating point number. 
# Store this floating point number in a variable. 
# Then print: (floating point number)  =  (the integer from the user). 
# Also print the type of the floating point variable.

# Get a number as input and cast it to a float
f = float(input("Enter a number: ")) 

# Cast f to an integer
i = int(f)

# Cast the variables to strings while displaying them
print(str(f) + " = " + str(i))

# Display the data type of f; should be float
print(type(f))
