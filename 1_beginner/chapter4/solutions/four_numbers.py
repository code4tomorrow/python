# Ask the user for 4 numbers. Use only 3 if else blocks to find the largest number. You may not use elifs
# For example, this counts as an if/else block
''' 

if(2 > 3):
	print("yay")
else:
	print("nay")

'''

#This question is really tricky, and requires some ingenuity.
#Write code here

a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))
d = float(input("Enter number 4: "))

max1 = -1
max2 = -1
max_f = -1

if(a > b):
	max1 = a
else:
	max1 = b

if( c > d):
	max2 = c
else:
	max2 = d

if(max1 > max2):
	max_f = max1
else:
	max_f = max2

print(max_f)