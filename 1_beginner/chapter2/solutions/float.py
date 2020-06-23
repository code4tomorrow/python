# Float
# Write a program that takes a number from the user
# and stores it in a variable. Cast the number to an
# integer and store in another variable.
# Then print: (floating point number) = (integer).
# Also print the type of the floating point variable.

# Get a number as input and cast it to a float
f = float(input("Enter a number: "))

# Cast f to an integer
i = int(f)

# Cast the variables to strings while displaying them
print(str(f) + " = " + str(i))

# Display the data type of f; should be float
print(type(f))
