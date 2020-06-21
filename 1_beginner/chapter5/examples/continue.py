# Continue
x = int(input("Enter a number: "))
while x < 20:
    # don't print the number if it
    # is divisible by 4
    if x % 4 == 0:
        x += 1
        continue
    print(x)
    x += 1
