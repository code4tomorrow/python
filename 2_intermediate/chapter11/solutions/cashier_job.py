# Write a function that will take the number of pennies, nickels, dimes,
# quarters, and discount(i.e. 15 for 15% discount). Return the total amount of
# money after discount.
#
# Print what is returned by the function after it is run with 97 pennies,
# 13 nickels, 18 dimes, 54 quarters, and 20% discount.
# Print what is returned by the function after it is run with 32 pennies,
# 19 nickels, 22 dimes, 71 quarters, and 51% discount.


def calc_total(penny, nickel, dime, quarter, discount):
    before_discount = (
        0.01 * penny + 0.05 * nickel + 0.1 * dime + 0.25 * quarter
    )
    discount_multiplier = 1 - discount * 0.01

    return round(before_discount * discount_multiplier, 2)


print(calc_total(97, 13, 18, 54, 20))

print(calc_total(32, 19, 22, 71, 51))
