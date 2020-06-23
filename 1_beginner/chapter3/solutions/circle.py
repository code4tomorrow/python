# Circle
# Write a program that asks the user for the radius of a circle.
# Then print the area and circumference of the circle.
# Store 3.14 as the value of pi, which is a constant.
# Don't forget to add comments!

PI = 3.14

# Prompt the user for a radius
radius = float(input("Enter a radius: "))

# Calculate the area and circumference
area = PI * radius ** 2
circumference = 2 * PI * radius

# Print the result
print("The area of the circle is ", area)
print("The circumference of the circle is ", circumference)
