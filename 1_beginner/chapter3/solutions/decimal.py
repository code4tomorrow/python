# Decimal
# Write a program that asks the user for a floating point number as input.
# It returns the decimal part (the part to the right of the decimal point).
# Don't worry about floating point errors! 
# The output should round to the correct answer, though.

# Get the floating point number input
num = float(input("Enter a floating point number: "))

# Cast float to int
int_num = int(num)

# Calculate decimal part
decimal = num - int_num

# Display result
print("The decimal part is " + str(decimal))

# Display result with rounding (optional)
rounded_decimal = round(decimal, 10)
print("The exact decimal part is " + str(rounded_decimal))
