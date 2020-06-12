#Get 3 numbers from the user. Find the biggest number and add them all together.
#If the sum is bigger than 2 times the biggest of the 3 numbers, then return the sum. 
#If it's smaller, multiply the sum by 3 and return the product.


x = int(input()) #first three numbers
y = int(input())
z = int(input())

s = x + y + z   # sum

if x > y and x>z: #figuring out the biggest number
    maxn = x
    
elif y > x and y > z:
        maxn = y
        
else: maxn = z
    
if s > 2 * maxn:       # compareing the sum and 2 times the biggest number
    print(s)
else: print(3*s)
   
