"""
Hoppity the Rabbit wrote some code, but it doesn't run correctly and he needs your help!
The following program is supposed to print a string based on a numerical input of the temperature. 
See if you can fix it for him!
"""
#I added some comments to aid you. Good luck! - Hoppity
temp = int(input("Enter temperature: ")) #possible input range is 0-100

if(temp < 100): #60-100 is hot
    print('hot')
if(temp <= 60): #30-59 is normal
    print('normal')
if(temp < 30): #0-29 is cold
    print('cold')
