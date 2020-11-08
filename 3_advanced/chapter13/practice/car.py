"""
A new car is said to devalue 20% in the first year. Assuming that
this trend continues and that mileage divided by 100 is all you
subtract from this adjusted price, make a class “car” that has at
least the attributes “year, original price (aka og price), and
mileage.” Also, follow these guidelines.

--When using str() on a car, it should return the year, original
  price, mileage, and adjusted price. 
--When adding, it should add the value to its mileage before
  adjusting the adjusted price. 
--When multiplying, it should multiply the mileage by the value
  before adjusting the adjusted price
--(While subtracting or dividing mileage on a car to sell it is
  totally unethical,) When subtracting or dividing, it should
  subtract the value from its mileage or divide its mileage by
  the value before adjusting the adjusted price.
--When checking gt(which means greater than), lt, ge, le, ne,
  and eq, it should compare the price with the other value.
--You should be able to compare cars (prices) but not add cars
  together

If you need help with modeling the equation for the adjusted price,
this may help

self.adjustedprice=self.ogprice * (0.8**(2020-self.year)))
self.adjustedprice=round((self.adjustedprice),2)-self.mileage/100

"""

# write your code below

