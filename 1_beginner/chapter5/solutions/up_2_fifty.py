# Write a program that takes a number from the user
# and adds 2 to it until it reaches 50 or more,
# then prints out how many times 2 was added.
# If the number is already greater than 50,
# then print out ('Already there!')

# prompt user for a number
x = int(input("Enter a number: "))

# initialize the counting variable
iterations = 0

# check if the number is less or greater than 50
if x < 50:    
    # while loop to get to 50 and 
    # count how many iterations
    while x < 50:       
        x += 2
        iterations += 1

    # print the number of iterations
    # once the loop is done running
    print(iterations)          
else: 
    print('Already there!')