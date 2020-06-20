# Write a program that asks for and reads an input from the user
#Then add all the numbers from 0 to that number up. You can use a for or while loop.
#Print out the sum

sum1 = 0
n = int(input("Please enter number "))
for i in range(n+1):
    sum1 += i
print("\n")
print("Sum is: ", sum1)
