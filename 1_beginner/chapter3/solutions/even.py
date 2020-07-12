# Even
# Write a program that takes an integer as input,
# and displays True if the integer is even.
# Otherwise, it displays False.

# Get integer input
i = int(input("Enter an integer: "))

# Display output
is_even = i % 2 == 0
print("Is this number even? " + str(is_even))
