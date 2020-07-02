'''
Create a program that takes a POSITIVE integer
as an input and checks if it is no greater than 100.
Print True if it is, and False if it isn't

YOU MAY NOT USE THE GREATER THAN or
LESS THAN OPERATORS (>, <, >=, or <=).
Find a way to do this problem only
using only the == operator and any math operators you want.
'''
x = int(input("Enter you number here. It must be positive: "))
print(x // 100 == 0)
