"""
Temperature
Hoppity the Rabbit wrote some code,
but it doesn't run correctly and he needs your help!
The following program is supposed to print a string
based on a numerical input of the temperature.
See if you can fix it for him!
"""

# assume possible input range is 0-100
temp = int(input("Enter temperature: "))

if 60 <= temp <= 100:  # 60-100 is hot
    print("hot")
if 30 <= temp < 60:  # 30-59 is normal
    print("normal")
if 0 <= temp < 30:  # 0-29 is cold
    print("cold")

# alternatively, you can also use elif
# if temp >= 60:
#     print('hot')
# elif temp >= 30:
#     print('normal')
# else:
#     print('cold')
