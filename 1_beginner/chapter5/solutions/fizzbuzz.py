# Fizz Buzz
"""
Credit to: https://www.youtube.com/watch?v=QPZ0pIK_wsc

Fizz Buzz is a game played between 2 people
where they take turns counting up starting at 1.
However, if the number is divisible by 3, the person
should say "fizz" instead of the number.
If the number is divisible by 5, the person should
say "buzz" instead of the number.
If the number is divisible by both 3 and 5,
the person should say "fizzbuzz" instead of the number.
For example, this is how the first 5 results would look like:
1
2
fizz
4
buzz
Write a program that outputs the first 100 results.
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
