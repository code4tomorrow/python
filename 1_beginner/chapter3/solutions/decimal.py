# Decimal
# Write a program that asks the user for a floating point number as input.
# It prints out the decimal part (the part to the right of the decimal point).
# Don't worry about floating point errors!
# Note: To display a more exact output, you can use
# rounded_decimal = round(decimal_variable, 10)
# to set rounded_decimal to your decimal_variable rounded to a precision
# of 10 decimal places.

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
