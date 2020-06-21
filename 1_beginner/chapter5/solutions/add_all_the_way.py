# Write a program that asks for and
# reads an input from the user
# Then add all the numbers up from 0
# to that number up. You can use a
# for or while loop. Print out the sum.

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
