"""
Create a recursive method that mirrors how a logarithm works in math.
You can have the base by default by ten. You do not have to deal
with decimals, just worry about returning integers.

Note: Logarithms return the power that you raise a base number to
in order to get a number.

Ex: logarithm of 9 to base 3 = 2; In this example, since 3 to the
2nd power gives you 9, the logarithm of 9 to base 3 is equal to 2.
"""

def logarithm(number, base=10, at=1, times=0):
    if number < 1 or base == 1:
        return None
    if number == 1:
        return 0
    if at > number:
        return times - 1
    if at == number:
        return times
    newcurrent = at * base
    return logarithm(number, base, newcurrent, times + 1)
