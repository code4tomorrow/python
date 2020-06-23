# Power
# Write a program that accepts two numbers, x and y.
# Compute and print the quantity (x + y) ^ 5. Display the entire equation.
# The program should accept decimals as inputs.

# Get the float inputs
x = float(input("Enter x: "))
y = float(input("Enter y: "))

# Calculate the answer
answer = (x + y) ** 5

# Display the equation and cast the numbers to strings
print("(" + str(x) + " + " + str(y) + ") ^ 5 = " + str(answer))
