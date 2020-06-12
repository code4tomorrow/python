#Write a program that takes a number from the user and adds 2 to it until it reaches 50 or more,
#then prints out how many times 2 was added.  
#If the number is already greater than 50, then print out (' Already there!')


x = int(input())  #input from user

c = 0             # initialize the counting variable


if x < 50:        # check if the number is less or greater than 50 
    while x < 50:       #while loop to get to 50 and count how many times
        x += 2
        c += 1 
    print(c)          # print the count
else: 
    print('Already there!') # print already there if x > 50

    


