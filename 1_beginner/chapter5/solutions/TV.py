# TV
# Pretend you just got a 50 on your test,
# and you mom says you can’t watch TV until you get
# a score of at least 80. (HINT: comparison operators).
# You increase your test score by 10 points per day.
# Write a program that tells you after
# how many days you'll be able to watch TV. Use a loop.

x = 50
days = 0
while x < 80:
    x += 10
    days += 1
print("You can watch TV after", days, "days")
