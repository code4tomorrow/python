# Get 3 numbers from the user. Find the biggest number and add them all together.
# If the sum is bigger than 2 times the biggest of the 3 numbers, then print the sum. 
# If it's smaller or equal, multiply the sum by 3 and print the product.

# prompt the user to enter 3 numbers
x = float(input("Enter number 1: "))
y = float(input("Enter number 2: "))
z = float(input("Enter number 3: "))

# calculate sum
sum = x + y + z  

# figuring out the biggest number
if x > y and x > z: 
    max = x
elif y > x and y > z:
    max = y
else: 
    max = z

# comparing the sum and 2 times the biggest number
if sum > 2 * max:
    print(sum)
else: 
    print(3 * sum)