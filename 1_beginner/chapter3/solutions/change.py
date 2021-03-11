"""
Write code that takes, as input, the number of dollars a person has
(a floating number), and outputs how much they have
in dollars, quarters, dimes, nickels and pennies.

For example, if someone has $4.62, the program would print the following:

4 dollars
2 quarters
1 dime
0 nickels
2 cents

The starting code is given.

Note: This is a challenge problem! Do not feel bad or disheartned if you can't
solve it. We will go over it next class.
"""

CENTS_PER_DOLLAR = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

# prompt user for dollars and convert it to cents
num_cents = int(float(input("How many dollars do you have: $")) * CENTS_PER_DOLLAR)

# calculate change and display it
dollars = num_cents // CENTS_PER_DOLLAR
remaining = num_cents % CENTS_PER_DOLLAR
print(dollars, "dollars")

quarters = remaining // CENTS_PER_QUARTER
remiaining = remaining % CENTS_PER_QUARTER
print(quarters, "quarters")

dimes = remaining // CENTS_PER_DIME
remiaining = remaining % CENTS_PER_DIME
print(dimes, "dimes")

nickels = remaining // CENTS_PER_NICKEL
remiaining = remaining % CENTS_PER_NICKEL
print(nickels, "nickels")

cents = remaining
print(cents, "cents")
