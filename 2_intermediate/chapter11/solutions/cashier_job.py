# Cashier Job
# Write a function called calculate_total
# that will take the number of pennies, nickels, dimes,
# quarters, and discount rate (i.e. 15 for 15% discount).
# Return the total amount of money after discount.
#
# Print what is returned by the function after it is run with 97 pennies,
# 13 nickels, 18 dimes, 54 quarters, and 20% discount.
# Print what is returned by the function after it is run with 32 pennies,
# 19 nickels, 22 dimes, 71 quarters, and 51% discount.


def calculate_total(penny, nickel, dime, quarter, discount):
    before_discount = 0.01 * penny + 0.05 * nickel + 0.1 * dime + 0.25 * quarter
    discount_multiplier = 1 - discount * 0.01

    # Round to 2 decimals since it is money
    return round(before_discount * discount_multiplier, 2)


print(calculate_total(97, 13, 18, 54, 20))

print(calculate_total(32, 19, 22, 71, 51))
