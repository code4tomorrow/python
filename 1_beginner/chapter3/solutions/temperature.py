  # Temperature
# Write a program that converts Celsius to Fahrenheit.
# It should ask the user for the temperature in
# degrees Celsius and then print the temperature in degrees Fahrenheit.
# The formula is: F = C * 9/5 + 32

# Get the Celsius value as input
celsius = float(input("Enter a temperature in degrees Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius * 9 / 5 + 32

# Display answer
print("The temperature in degrees Fahrenheit is " + str(fahrenheit))
