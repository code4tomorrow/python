# Add All the Way
# Take a number from the user and
# add every number up from 1 to that number.
# Print the result.
# You can use a for or while loop.

# for loop solution
sum = 0
n = int(input("Please enter a number: "))
for i in range(1, n + 1):
    sum += i
print("Sum is:", sum)

# while loop solution
# sum = 0
# count = 1
# n = int(input("Please enter a number: "))
# while count <= n:
#     sum += count
#     count += 1
# print("Sum is:", sum)
