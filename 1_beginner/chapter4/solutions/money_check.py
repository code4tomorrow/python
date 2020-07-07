# Money Check
# Write a program that asks for a person's
# amount of money (floating point).
# If the person's amount of money is 0,
# print "Bankrupt". If not, print "Not Bankrupt"
# If the person's amount of money is
# greater than 1000.0, then print "Rich".

money = float(input("Enter the amount of money you have: $"))

if money == 0:
    print("Bankrupt")
else:
    print("Not Bankrupt")

if money > 1000:
    print("Rich")
