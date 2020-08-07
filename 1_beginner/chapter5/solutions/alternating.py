"""
Alternating
Ask the user for an integer. The print the numbers from 1
to that number, but alternating in sign. For example, if the input
was 5, what would be printed is 1, -1, 2, -2, 3, -3, 4, -4, 5.
(Note, DO NOT include the last negative number).
Do this with a for loop
"""

# Write code here.

number = int(input("Enter Number Here: "))
for num in range(1,number+1):
    if num == number:
        print(num)
    else:
        print(num)
        print(-1*num)



# Now try it with a while loop
number = int(input("Enter Number Here: "))
current_num = 1
while(current_num < number):
    print(current_num)
    print(-1 *current_num)
    current_num+= 1
print(current_num)

