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

num_cents = int(
    float(input("How many dollars do you have: $")) * CENTS_PER_DOLLAR
)

# What do you do next? Write code here
